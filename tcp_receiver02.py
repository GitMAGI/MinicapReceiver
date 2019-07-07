import socket
import log00 as log_lib
import utils00 as utils_lib
import time

def tcp_receiver(queue, remote_addr, remote_port, chunk_size = 4096, sleeping_time = 0.000001, queue_max_counter = 5):    
    log_lib.debug("Starting ...")
    start_time = time.time()

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

        window_name = str(pid) + " " + str(virtual_width) + "x" + str(virtual_height)                
        while True: 
            log_lib.debug("Current Queue size {}".format(queue.qsize())) 

            if queue.qsize == 0:                          
                time.sleep(sleeping_time)
                continue

            if queue.qsize() > queue_max_counter:
                break
            
            frame_size_bytes = sock.recv(4)
            frame_size = int.from_bytes(frame_size_bytes, byteorder='little', signed=False)
            frame_data = sock.recv(frame_size)
            log_lib.debug("Received a frame of size of {} B. Expected frame size was {} B".format(len(frame_data), frame_size))            
            queue.put(frame_data)
            log_lib.debug("Added data to Queue. Current Queue size {}".format(queue.qsize()))
            time.sleep(sleeping_time)
            

    except Exception as e:
        log_lib.fatal(str(e))
    finally:
        log_lib.info("Closing TCP socket {}:{} ...".format(remote_addr, remote_port))
        sock.close()   

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))