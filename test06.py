import time
import socket
from queue import Queue, LifoQueue
from threading import Thread, Event
from log02 import Log
import utils00 as utils_lib
import tcp_receiver02 as receiver_lib
import data_processing00 as processing_lib
import process_monitoring00 as monitoring_lib

log_lib = Log.get_instance()

def test():
    log_lib.info("Starting ...")
    start_time = time.time()
    
    main_loop_sleeping_time = 0.0001

    receiver_worker_sleeping_time = 0.0001
    processing_worker_sleeping_time = 0.0001
    viewer_worker_sleeping_time = 0.0001
    monitoring_worker_sleeping_time = 0.0001

    remote_addr = 'localhost'
    remote_port = 1717

    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (remote_addr, remote_port)
        log_lib.info("Starting TCP Connection to {}:{} ...".format(remote_addr, remote_port))
        sock.connect(server_address)
        log_lib.info("TCP Connection to {}:{} successfully established!".format(remote_addr, remote_port))

        # Retrieve Global Header Informartions
        #time.sleep(sleeping_time)
        globalHeader = sock.recv(24)

        version = globalHeader[0]
        header_size = globalHeader[1]
        pid = int.from_bytes(globalHeader[2:5], byteorder='little', signed=False)
        real_width = int.from_bytes(globalHeader[6:9], byteorder='little', signed=False)
        real_height = int.from_bytes(globalHeader[10:13], byteorder='little', signed=False)
        virtual_width = int.from_bytes(globalHeader[14:17], byteorder='little', signed=False)
        virtual_height = int.from_bytes(globalHeader[18:21], byteorder='little', signed=False)
        display_orientation = globalHeader[22]
        quirk_flag = globalHeader[23]

        log_lib.info("Information from the Server: version {}".format(version))
        log_lib.info("Information from the Server: header_size {}".format(header_size))
        log_lib.info("Information from the Server: pid {}".format(pid))
        log_lib.info("Information from the Server: real_width {}".format(real_width))
        log_lib.info("Information from the Server: real_height {}".format(real_height))
        log_lib.info("Information from the Server: virtual_width {}".format(virtual_width))
        log_lib.info("Information from the Server: virtual_height {}".format(virtual_height))
        log_lib.info("Information from the Server: display_orientation {}".format(display_orientation))
        log_lib.info("Information from the Server: quirk_flag {}".format(quirk_flag))

        window_name = str(pid) + " " + str(virtual_width) + "x" + str(virtual_height)

        q_in = LifoQueue()
        q_out = LifoQueue()

        log_lib.info("Worker {} sleeping time {}".format('RECEIVER', receiver_worker_sleeping_time))
        log_lib.info("Worker {} sleeping time {}".format('PROCESSING', processing_worker_sleeping_time))
        log_lib.info("Worker {} sleeping time {}".format('VIEWER', viewer_worker_sleeping_time))
        log_lib.info("Worker {} sleeping time {}".format('MONITORING', monitoring_worker_sleeping_time))

        # Thread for retrieving data from TCP
        receiver_worker_stop = Event()
        receiver_worker = Thread(target=receiver_lib.tcp_receiver, args=(receiver_worker_stop, q_in, sock, receiver_worker_sleeping_time, ))
        receiver_worker.setDaemon(False)
        receiver_worker.start()

        time.sleep(main_loop_sleeping_time)

        # Thread for Processing
        processing_worker_stop = Event()
        processing_worker = Thread(target=processing_lib.frame_processor, args=(processing_worker_stop, q_in, q_out, processing_worker_sleeping_time, ))
        processing_worker.setDaemon(False)
        processing_worker.start()    
   
        time.sleep(main_loop_sleeping_time)

        # Thread for Displaying frames
        viewer_worker_stop = Event()
        viewer_worker = Thread(target=processing_lib.frame_viewer, args=(viewer_worker_stop, q_out, viewer_worker_sleeping_time, ))
        viewer_worker.setDaemon(False)
        viewer_worker.start()    
   
        time.sleep(main_loop_sleeping_time)

        # Thread for Monitoring queues status
        monitoring_worker_stop = Event()
        monitoring_worker = Thread(target=monitoring_lib.queues_monitoring, args=(monitoring_worker_stop, q_in, q_out, monitoring_worker_sleeping_time, ))
        monitoring_worker.setDaemon(False)
        monitoring_worker.start()    
   
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
        processing_worker.join()
        log_lib.info("Processing Thread is done!")

        time.sleep(0.2)

        viewer_worker_stop.set()
        log_lib.info("Viewer Thread terminating ...")  
        viewer_worker.join()
        log_lib.info("Viewer Thread is done!")

        time.sleep(0.2)

        monitoring_worker_stop.set()
        log_lib.info("Monitoring Thread terminating ...")  
        monitoring_worker.join()
        log_lib.info("Monitoring Thread is done!")

        time.sleep(0.2)

    except Exception as e:
        log_lib.fatal(str(e))

    finally:
        pass

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

    return