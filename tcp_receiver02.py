import log00 as log_lib
import utils00 as utils_lib
import time

def tcp_receiver(stop_event, queue, sock, sleeping_time = 0.001):    
    log_lib.debug("Starting ...")
    start_time = time.time()

    while not stop_event.is_set():
        log_lib.debug("Current Queue size {}".format(queue.qsize()))        
        frame_size_bytes = sock.recv(4)
        frame_size = int.from_bytes(frame_size_bytes, byteorder='little', signed=False)
        #time.sleep(sleeping_time)
        frame_data = sock.recv(frame_size)
        log_lib.debug("Received a frame of size of {} B. Expected frame size was {} B".format(len(frame_data), frame_size))            
        queue.put(frame_data)
        log_lib.debug("Added data to Queue. Current Queue size {}".format(queue.qsize()))
        time.sleep(sleeping_time)

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))