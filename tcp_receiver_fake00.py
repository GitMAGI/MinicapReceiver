from log02 import Log
import utils00 as utils_lib
import time
import os
import subprocess
import re

log_lib = Log.get_instance()

def tcp_receiver(stop_event, queue, sock, sleeping_time = 0.001):
    log_lib.info("Starting ...")
    start_time = time.time()

    input_path = 'input'
    input_filename = '20190827_215900.mp4'
    w = int(1920/5)
    h = int(1080/5)

    # Command for extract a sequence of jpgs from a video file
    # ffmpeg -i .\input\video.mp4 -c:v mjpeg -f image2pipe -s Width x Height pipe:1
    input_fullfilename = os.path.join(input_path, input_filename)
    cmd = [
        'ffmpeg', '-i', input_fullfilename, '-c:v', 'mjpeg', '-q:v', '1', '-f', 'image2pipe', '-s', '{}x{}'.format(w, h), 'pipe:1'
    ]
    input_process = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
    [input_data, input_err] = input_process.communicate(input = input_process)
    if input_err:
        log_lib.fatal(input_err)
        return
    log_lib.debug("Got %d Bytes of data" % len(input_data))

    # Gather an array of JPGs
    # A JPG is delimited by 2 Sequences:
    #  SOI (Start of Image) 0xFF 0xD8
    #  EOI (End of Image)   0xFF 0xD9
    frames = []
    soi_pattern = br'\xFF\xD8'
    regex = re.compile(soi_pattern)
    start_indexes = [m.start(0) for m in re.finditer(soi_pattern, input_data)]

    #print(start_indexes)
    #print(len(start_indexes))

    eoi_pattern = br'\xFF\xD9'
    regex = re.compile(eoi_pattern)
    end_indexes = [m.end(0) for m in re.finditer(eoi_pattern, input_data)]

    #print(end_indexes)
    #print(len(end_indexes))

    for i in range(0, len(start_indexes), 1):
        start = start_indexes[i]
        end = end_indexes[i]
        frame_data = input_data[start:end]
        frames.append(frame_data)

    log_lib.debug("Extracted %d jpg frames" % len(frames))

    i = 0
    while not stop_event.is_set():
        if i >= len(frames):
            i = 0
        frame_data = frames[i]
        log_lib.debug("Current Queue size {}".format(queue.qsize())) 
        log_lib.debug("Received a frame of size of {} B. Expected frame size was {} B".format(len(frame_data), len(frame_data))) 
        queue.put(frame_data)
        log_lib.debug("Added data to Queue. Current Queue size {}".format(queue.qsize()))
        i += 1
        time.sleep(sleeping_time)                

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))