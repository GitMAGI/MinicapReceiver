from threading import Thread, Event
from queue import Queue, LifoQueue
import time
import socket
import log00 as log_lib
import utils00 as utils_lib
import numpy as np
import cv2

class TCPProcessingThread(Thread):
    def __init__(self, socket, queue, sleeping_time = 0.00001):
        Thread.__init__(self)
        self.queue = queue
        self.socket = socket
        self.sleeping_time = sleeping_time
        self.stop_event = Event()

    def run(self):
        log_lib.debug("Starting ...")
        start_time = time.time()
        
        while not self.stop_event.is_set():
            try:
                log_lib.debug("Trying to pull data from Queue. Current Queue size {}".format(queue.qsize()))
                if queue.qsize() == 0:           
                    time.sleep(sleeping_time)
                    continue

                frame_data = queue.get(block = True)
                log_lib.debug("Pulled a frame of size of {} B from Queue. Current Queue size {}".format(len(frame_data), queue.qsize()))                
                frame = cv2.imdecode(np.fromstring(frame_data, dtype = np.uint8), -1) 
                cv2.wait(0)
                cv2.imshow('Window', frame)            

                time.sleep(sleeping_time)

            except Exception as e:
                log_lib.fatal(str(e)) 
                break

        try:
            cv2.destroyAllWindows()
        except:
            pass

        elapsed_time = time.time() - start_time
        log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))
    
    def stop(self):
        self.stop_event.set()
        log_lib.info("Thread is terminating ...")    
        self.join()
        log_lib.info("Thread is done!")  