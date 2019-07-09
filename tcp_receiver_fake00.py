import log00 as log_lib
import utils00 as utils_lib
import time
import os

def tcp_receiver(stop_event, queue, sock, sleeping_time = 0.000001):
    log_lib.debug("Starting ...")
    start_time = time.time()

    input_path = ''
    input_filename = ''
    w = 0
    h = 0

    input_fullfilename = os.path.join(input_path, input_filename)
    cmd = [
        'ffmpeg', '-i', input_fullfilename, '-c:v', 'h264', '-f', 'h264', 'pipe:1'
    ]
    input_process = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE)
    [input_data, input_err] = input_process.communicate(input = input_process)
    if input_err:
        log_lib.fatal(input_err)
        return
    print("Got %d Bytes of data" % len(input_data))

    time.sleep(.2)

    while not stop_event.is_set():
        while True:
            pass
        pass

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))