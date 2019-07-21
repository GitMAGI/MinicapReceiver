import time
import os
import sys
import utils00 as utils_lib
from log02 import Log
import test00
import test01
import test02
import test03
import test04
import test05
import test06

basename = os.path.basename(__file__)
log_lib = Log.get_instance()
log_lib.set_min_level(1)

def main():
    log_lib.info("Starting ...")
    start_time = time.time()

    for arg in sys.argv[1:]:
        pass

    #time.sleep(0.234)  

    #test00.test()

    # Receive, process and display from devices!
    #test01.test()

    # Not Implemented yet!
    #test02.test()

    # FAKE RECEIVER (Reads a Video from file)
    #test03.test()

    # Test Logging on different streams
    #test04.test()

    # Test Logging with replace line
    #test05.test()

    # Test Receive, process and display from devices, showing Queue status
    test06.test()

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

if __name__ == "__main__":
    main()