from threading import Thread, Event
from queue import Queue, LifoQueue
import time
import socket
import log00 as log_lib
import utils00 as utils_lib

class TCPReceiverThread(Thread):
    def __init__(self, socket, queue, sleeping_time = 0.001):
        Thread.__init__(self)
        self.queue = queue
        self.socket = socket
        self.sleeping_time = sleeping_time
        self.stop_event = Event()

    def run(self):
        log_lib.debug("Starting ...")
        start_time = time.time()

        try:
            while not self.stop_event.is_set():
                frame_size_bytes = self.socket.recv(4)
                frame_size = int.from_bytes(frame_size_bytes, byteorder='little', signed=False)
                frame_data = self.socket.recv(frame_size)
                log_lib.debug("Received a frame of size of {} B. Expected frame size was {} B".format(len(frame_data), frame_size))            
                self.queue.put(frame_data)
                log_lib.debug("Added data to Queue. Current Queue size {}".format(queue.qsize()))
                time.sleep(self.sleeping_time)

        except Exception as e:
            log_lib.fatal(str(e))            
        finally:
            elapsed_time = time.time() - start_time
            log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))
    
    def stop(self):
        self.stop_event.set()
        log_lib.info("Thread is terminating ...")    
        self.join()
        log_lib.info("Thread is done!")        