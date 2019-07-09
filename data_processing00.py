import log00 as log_lib
import utils00 as utils_lib
import time
from queue import Queue
import numpy as np
import cv2


def frame_viewer(stop_event, queue, sleeping_time = 0.00001):
    log_lib.debug("Starting ...")
    start_time = time.time()

    while not stop_event.is_set():
        try:
            log_lib.debug("Trying to pull data from Queue. Current Queue size {}".format(queue.qsize()))
            if queue.qsize() == 0:           
                time.sleep(sleeping_time)
                continue

            frame_data = queue.get(block = False)
            log_lib.debug("Pulled a frame of size of {} B from Queue. Current Queue size {}".format(len(frame_data), queue.qsize()))         
            frame = cv2.imdecode(np.fromstring(frame_data, dtype = np.uint8), -1) 
            cv2.waitKey(0)
            cv2.imshow('Window', frame)

            #time.sleep(sleeping_time)
        except Exception as e:
            log_lib.error(str(e))
            break

    try:
        cv2.destroyAllWindows()
    except:
        pass
    
    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))