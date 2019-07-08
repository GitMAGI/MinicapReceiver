import time
import log00 as log_lib
import utils00 as utils_lib
import tcp_receiver01 as receiver_lib

def test():
    log_lib.debug("Starting ...")
    start_time = time.time()

    remote_addr = 'localhost'
    remote_port = 1717

    receiver_lib.tcp_receiver(remote_addr, remote_port)

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

    return