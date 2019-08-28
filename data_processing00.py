from log02 import Log
import utils00 as utils_lib
import time
from queue import Queue, Empty
import numpy as np
import cv2

log_lib = Log.get_instance()

def frame_viewer(stop_event, queue, sleeping_time = 0.0001):
    log_lib.debug("Starting ...")
    start_time = time.time()

    while not stop_event.is_set():
        try:
            log_lib.debug("Trying to pull data from Queue. Current Queue size {}".format(queue.qsize()))
            if queue.qsize() == 0:           
                time.sleep(sleeping_time)
                continue

            frame = queue.get(block = True)
            time.sleep(sleeping_time)
            log_lib.debug("Pulled a frame of size of {} B from Queue. Current Queue size {}".format(len(frame), queue.qsize()))            
            cv2.imshow('Window', frame)
            cv2.waitKey(1)

        except Exception as e:
            log_lib.error(str(e))
            break

    try:
        cv2.destroyAllWindows()
    except:
        pass
    
    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

def frame_processor(stop_event, queue_in, queue_out, sleeping_time = 0.0001):
    log_lib.debug("Starting ...")
    start_time = time.time()

    while not stop_event.is_set():
        try:
            log_lib.debug("Trying to pull data from the Input Queue. Current Input Queue size {}".format(queue_in.qsize()))
            if queue_in.qsize() == 0:           
                time.sleep(sleeping_time)
                continue

            frame_data = queue_in.get(block = True)
            log_lib.debug("Pulled a frame of size of {} B from Input Queue. Current Input Queue size {}".format(len(frame_data), queue_in.qsize()))         
            frame = cv2.imdecode(np.fromstring(frame_data, dtype = np.uint8), -1)

            # Give just last frame to the viewer
            while queue_out.qsize() > 0:
                try:
                    queue_out.get(False)
                except Empty:
                    continue

            queue_out.put(frame)
            log_lib.debug("Added data to Output Queue. Current Output Queue size {}".format(queue_out.qsize()))

            time.sleep(sleeping_time)
        
        except Exception as e:
            log_lib.error(str(e))
            break
    
    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))