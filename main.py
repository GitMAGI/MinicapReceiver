import time
import os
import sys
import utils00 as utils_lib
#import tcp_receiver00 as receiver_lib
import tcp_receiver01 as receiver_lib
import log00 as log_lib

basename = os.path.basename(__file__)

def main():
    log_lib.info("Starting ...")
    start_time = time.time()

    for arg in sys.argv[1:]:
        pass

    #time.sleep(0.234)  
    test00()

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

def test00():
    remote_addr = 'localhost'
    remote_port = 1717

    receiver_lib.tcp_receiver(remote_addr, remote_port)

    return

if __name__ == "__main__":
    main()