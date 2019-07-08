import time
import os
import sys
import utils00 as utils_lib
import log00 as log_lib
import test00
import test01
import test02

basename = os.path.basename(__file__)

def main():
    log_lib.info("Starting ...")
    start_time = time.time()

    for arg in sys.argv[1:]:
        pass

    #time.sleep(0.234)  

    #test00.test()
    test01.test()
    #test02.test()

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

if __name__ == "__main__":
    main()