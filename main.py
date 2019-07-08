import time
import os
import sys
import utils00 as utils_lib
import log00 as log_lib
import test00
import test01
import test03

basename = os.path.basename(__file__)

def main():
    log_lib.info("Starting ...")
    start_time = time.time()

    for arg in sys.argv[1:]:
        pass

    #time.sleep(0.234)  

    #test00.test00()
    #test01.test01()
    test03.test03()

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))


if __name__ == "__main__":
    main()