import socket
import log00 as log_lib
import time
import struct

def tcp_receiver(remote_addr, remote_port, sleeping_time = 0.0001):    
    try:
        # Create a TCP/IP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = (remote_addr, remote_port)
        log_lib.info("Starting TCP Connection to {}:{} ...".format(remote_addr, remote_port))
        sock.connect(server_address)
        log_lib.info("TCP Connection to {}:{} successfully established!".format(remote_addr, remote_port))

        # Retrieve Global Header Informartions
        time.sleep(sleeping_time)
        globalHeader = sock.recv(24)
        version = globalHeader[0]
        header_size = globalHeader[1]        

        pid = int.from_bytes(globalHeader[2:5], byteorder='little', signed=False)
        real_width = int.from_bytes(globalHeader[6:9], byteorder='little', signed=False)
        real_height = int.from_bytes(globalHeader[10:13], byteorder='little', signed=False)
        virtual_width = int.from_bytes(globalHeader[14:17], byteorder='little', signed=False)
        virtual_hieght = int.from_bytes(globalHeader[18:21], byteorder='little', signed=False)

        display_orientation = globalHeader[22]
        quirk_flag = globalHeader[23]
        
        log_lib.debug("Version: {}".format(version))
        log_lib.debug("Header Size: {}".format(header_size))
        log_lib.debug("PID: {}".format(pid))
        log_lib.debug("Real Width: {}".format(real_width))
        log_lib.debug("Real Height: {}".format(real_height))
        log_lib.debug("Virtual Width: {}".format(virtual_width))
        log_lib.debug("Virtual Height: {}".format(virtual_hieght))
        log_lib.debug("Display Orientation: {}".format(display_orientation))
        log_lib.debug("Quirk Flag: {}".format(quirk_flag))        

        debug_counter = 0
        amount_received = 0
        while True:
            time.sleep(sleeping_time)
            frame_size_bytes = sock.recv(4)
            frame_size = int.from_bytes(frame_size_bytes, byteorder='little', signed=False)
            time.sleep(sleeping_time)            
            frame_data = sock.recv(frame_size)
            amount_received += len(frame_data)
            log_lib.debug("Received a frame of size of {} B. Expected frame size was {}B. Total amount data received so far is {} B".format(len(frame_data), frame_size, amount_received))
            
            debug_counter += 1
            if debug_counter > 30:
                break

    except Exception as e:
        log_lib.fatal(str(e))
    finally:
        log_lib.info("Closing TCP socket {}:{} ...".format(remote_addr, remote_port))
        sock.close()   

    return