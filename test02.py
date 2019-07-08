import socket
import time
from queue import Queue, LifoQueue
from threading import Thread
import tcp_receiver02 as receiver_lib
import data_processing01 as processing_lib
import log00 as log_lib
import utils00 as utils_lib

main_loop_sleeping_time = 0.00001

def test():
    log_lib.debug("Starting ...")
    start_time = time.time()

    try:
        remote_addr = 'localhost'
        remote_port = 1717

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

        window_name = str(pid) + " " + str(virtual_width) + "x" + str(virtual_height)  

         # Thread for retrieving data from TCP

        time.sleep(main_loop_sleeping_time)

        # Thread for Processing/Displaying frames

        time.sleep(main_loop_sleeping_time)

        while True:
            time.sleep(main_loop_sleeping_time)

    except KeyboardInterrupt:
        log_lib.info("Keyboard interrupt received. Terminating ...")
    except Exception as e:
        log_lib.fatal(str(e))
    finally:
        log_lib.info("Closing TCP socket {}:{} ...".format(remote_addr, remote_port))
        sock.close()   

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))
