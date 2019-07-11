import time
import socket
from queue import Queue, LifoQueue
from threading import Thread, Event
import log00 as log_lib
import utils00 as utils_lib
import tcp_receiver_fake00 as receiver_lib
import data_processing00 as processing_lib

def test():
    log_lib.debug("Starting ...")
    start_time = time.time()

    main_loop_sleeping_time = 0.001
    try:
        q_in = LifoQueue()
        q_out = LifoQueue()

        # Thread for retrieving data from TCP
        receiver_worker_stop = Event()
        receiver_worker = Thread(target=receiver_lib.tcp_receiver, args=(receiver_worker_stop, q_in, None,))
        receiver_worker.setDaemon(False)
        receiver_worker.start()

        time.sleep(main_loop_sleeping_time)

        # Thread for Processing
        processing_worker_stop = Event()
        processing_worker = Thread(target=processing_lib.frame_processor, args=(processing_worker_stop, q_in, q_out,))
        processing_worker.setDaemon(False)
        processing_worker.start()    
   
        time.sleep(main_loop_sleeping_time)

        # Thread for Displaying frames
        viewer_worker_stop = Event()
        viewer_worker = Thread(target=processing_lib.frame_viewer, args=(viewer_worker_stop, q_out,))
        viewer_worker.setDaemon(False)
        viewer_worker.start()    
   
        time.sleep(main_loop_sleeping_time)

        while True:
            time.sleep(main_loop_sleeping_time)

    except KeyboardInterrupt:
        log_lib.info("Keyboard interrupt received. Terminating ...")

        receiver_worker_stop.set()
        log_lib.info("Receiver Thread terminating ...")        
        receiver_worker.join()
        log_lib.info("Receiver Thread is done!")

        time.sleep(0.2)
         
        processing_worker_stop.set()
        log_lib.info("Processing Thread terminating ...")  
        receiver_worker.join()
        log_lib.info("Processing Thread is done!")

        time.sleep(0.2)

        viewer_worker_stop.set()
        log_lib.info("Viewer Thread terminating ...")  
        viewer_worker.join()
        log_lib.info("Viewer Thread is done!")

        time.sleep(0.2)

    except Exception as e:
        log_lib.fatal(str(e))

    finally:
        pass

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

    return