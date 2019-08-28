from log02 import Log
import utils00 as utils_lib
import time

log_lib = Log.get_instance()

def queues_monitoring(stop_event, queue_in, queue_out, sleeping_time = 0.0001):
    log_lib.info("Starting ...")
    start_time = time.time()

    while not stop_event.is_set():
        log_lib.info("Input Queue size: %d | Output Queue size: %d" % (queue_in.qsize(), queue_out.qsize()), overwrite=True)
        time.sleep(sleeping_time)                

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

    return