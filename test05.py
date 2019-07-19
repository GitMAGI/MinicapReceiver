import time
from log02 import Log
import utils00 as utils_lib

log_lib = Log()
log_lib.min_level = 0

def test():
    log_lib.info("Starting ...")
    start_time = time.time()

    try:
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 1", overwrite=True)
        log_lib.error("Test Line Test Line Test Line Test Line Line Test Line Test Line 2")
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 3", overwrite=True)
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 4")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 5", overwrite=True)
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 6", overwrite=True)
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 7", overwrite=True)
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 8", overwrite=True)
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 9", overwrite=True)
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 10")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 11", overwrite=True)
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 12", overwrite=True)
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 13", overwrite=True)
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 14")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 15", overwrite=True)
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 16", overwrite=True)
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 17")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 18", overwrite=True)
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 19", overwrite=True)
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 20", overwrite=True)
        log_lib.error("Test Line Test Line Test Line Test Line Line Test Line Test Line 21")
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 22", overwrite=True)
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 23")
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 24", overwrite=True)
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 25")
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 26", overwrite=True)
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 27", overwrite=True)
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 28", overwrite=True)
        log_lib.error("Test Line Test Line Test Line Test Line Line Test Line Test Line 29")
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 30")

    except KeyboardInterrupt:
        log_lib.info("Keyboard interrupt received. Terminating ...")

    except Exception as e:
        log_lib.fatal(str(e))

    finally:
        pass

    elapsed_time = time.time() - start_time
    log_lib.info("Completed in %s" % utils_lib.elapsed_time_string(elapsed_time))

    return