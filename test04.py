import time
import log01 as log_lib
import utils00 as utils_lib

log_lib.min_level = 0

def test():
    log_lib.info("Starting ...")
    start_time = time.time()

    try:
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 1")
        log_lib.error("Test Line Test Line Test Line Test Line Line Test Line Test Line 2")
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 3")
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 4")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 5")
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 6")
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 7")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 8")
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 9")
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 10")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 11")
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 12")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 13")
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 14")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 15")
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 16")
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 17")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 18")
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 19")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 20")
        log_lib.error("Test Line Test Line Test Line Test Line Line Test Line Test Line 21")
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 22")
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 23")
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 24")
        log_lib.fatal("Test Line Test Line Test Line Test Line Line Test Line Test Line 25")
        log_lib.warning("Test Line Test Line Test Line Test Line Line Test Line Test Line 26")
        log_lib.debug("Test Line Test Line Test Line Test Line Line Test Line Test Line 27")
        log_lib.info("Test Line Test Line Test Line Test Line Line Test Line Test Line 28")
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