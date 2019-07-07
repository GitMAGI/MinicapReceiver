import time
import os
import sys
import utils00 as utils_lib
#import tcp_receiver00 as receiver_lib
#import tcp_receiver01 as receiver_lib
import tcp_receiver02 as receiver_lib
import data_processing00 as processing_lib
import log00 as log_lib

from queue import Queue, LifoQueue
from threading import Thread

basename = os.path.basename(__file__)

def main():
    log_lib.info("Starting ...")
    start_time = time.time()

    for arg in sys.argv[1:]:
        pass

    #time.sleep(0.234)  
    #test00()
    test01()

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

def test00():
    remote_addr = 'localhost'
    remote_port = 1717

    receiver_lib.tcp_receiver(remote_addr, remote_port)

    return

def test01():
    remote_addr = 'localhost'
    remote_port = 1717

    q = LifoQueue()

    # Thread for retrieving data from TCP
    receiver_worker = Thread(target=receiver_lib.tcp_receiver, args=(q, remote_addr, remote_port,))
    receiver_worker.setDaemon(False)
    receiver_worker.start()

    time.sleep(0.1)

    # Thread for Processing/Displaying frames
    processing_worker = Thread(target=processing_lib.frame_viewer, args=(q,))
    processing_worker.setDaemon(False)
    processing_worker.start()

    # Join Threads
    processing_worker.join()
    receiver_worker.join()

    return

if __name__ == "__main__":
    main()