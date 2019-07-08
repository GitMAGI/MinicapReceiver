import tcp_receiver02 as receiver_lib
import data_processing00 as processing_lib

from queue import Queue, LifoQueue
from threading import Thread

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