import log00 as log_lib
import time
from queue import Queue, LifoQueue
from threading import Thread
import tcp_receiver02 as receiver_lib
import data_processing00 as processing_lib

main_loop_sleeping_time = 0.00001

def test03():
    try:
        q = LifoQueue()

        remote_addr = 'localhost'
        remote_port = 1717

        # Thread for retrieving data from TCP
        #receiver_worker = Thread(target=receiver_lib.tcp_receiver, args=(q, remote_addr, remote_port,))
        #receiver_worker.setDaemon(False)
        #receiver_worker.start()

        time.sleep(0.1)

        # Thread for Processing/Displaying frames
        #processing_worker = Thread(target=processing_lib.frame_viewer, args=(q,))
        #processing_worker.setDaemon(False)
        #processing_worker.start()

        while True:
            log_lib.debug("Looping like a bomber!")

            time.sleep(main_loop_sleeping_time)
        
    except KeyboardInterrupt:
        log_lib.info("Keyboard interrupt received. Terminating ...")
        pass
    
    return