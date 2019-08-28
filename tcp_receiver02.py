from log02 import Log
import utils00 as utils_lib
import time

log_lib = Log.get_instance()

def tcp_receiver(stop_event, queue, sock, sleeping_time = 0.0001):    
    log_lib.debug("Starting ...")
    start_time = time.time()

    while not stop_event.is_set():
        log_lib.debug("Current Queue size {}".format(queue.qsize()))  

        frame_size_bytes = b''
        len_frame_size_bytes = 0
        while len_frame_size_bytes < 4:
            frame_size_bytes_left_to_recv = 4 - len_frame_size_bytes
            tmp_frame_size_bytes = sock.recv(frame_size_bytes_left_to_recv)
            frame_size_bytes += tmp_frame_size_bytes
            len_frame_size_bytes = len(frame_size_bytes)
        if frame_size_bytes == b'':
            raise Exception("Bad data received on socket. Got no bytes for Frame Size")
        frame_size = int.from_bytes(frame_size_bytes, byteorder='little', signed=False)

        frame_data = b''
        len_frame_data = 0
        while len_frame_data < frame_size:
            frame_data_left_to_recv = frame_size - len_frame_data
            tmp_frame_data = sock.recv(frame_data_left_to_recv)
            frame_data += tmp_frame_data
            len_frame_data = len(frame_data)    
        if frame_data == b'':
            log_lib.error("Bad data recevid on socket. Got no bytes for an Expected Frame of size {}".format(frame_size))
        
        log_lib.debug("Received a frame of size of {} B. Expected frame size was {} B".format(len(frame_data), frame_size))

        # Give just last frame to the processor
        while queue.qsize() > 0:
            try:
                queue.get(False)
            except Empty:
                continue

        queue.put(frame_data)
        log_lib.debug("Added data to Queue. Current Queue size {}".format(queue.qsize()))

        time.sleep(sleeping_time)

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))