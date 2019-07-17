import enum
import datetime
import sys
import inspect

min_level = -1

def _log_line(stream, type, caller_filename, caller_function, data):
    try:
        if type.value < min_level:
            return

        current_time_str = str(datetime.datetime.now())
        type_str = type.name.capitalize()
        line = "{} | {} | {} @ {} >>> {}".format(current_time_str, type_str, caller_function, caller_filename, data)
        #line = "{}\t{}\t{}\t{}\t{}".format(current_time_str, type_str, caller_function, caller_filename, data)

        stream.write("%s\n" % line)
    except:
        sys.stderr.write("Erorr during the log operation\n")
        sys.stderr.flush()
    return

def debug(msg, data = None):
    caller_filename = "--unknown--"
    stack = inspect.stack()
    try:
        frame = stack[1]
        module = inspect.getmodule(frame[0])
        caller_filename = module.__file__
    except:
        pass

    caller_function = "--unknown--"
    try:           
        the_class = stack[1][0].f_locals["self"].__class__
        the_method = stack[1][0].f_code.co_name
        caller_function = the_class + "." + the_method
    except:
        try:    
            caller_function = inspect.getouterframes(inspect.currentframe(), 2)[1][3]
        except:
            pass

    stream = sys.stdout
    _log_line(stream, LogType.debug, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(stream, LogType.debug, caller_filename, caller_function, str(data))
    return

def info(msg, data = None):
    caller_filename = "--unknown--"
    stack = inspect.stack()
    try:
        frame = stack[1]
        module = inspect.getmodule(frame[0])
        caller_filename = module.__file__
    except:
        pass

    caller_function = "--unknown--"
    try:           
        the_class = stack[1][0].f_locals["self"].__class__
        the_method = stack[1][0].f_code.co_name
        caller_function = the_class + "." + the_method
    except:
        try:    
            caller_function = inspect.getouterframes(inspect.currentframe(), 2)[1][3]
        except:
            pass

    stream = sys.stdout
    _log_line(stream, LogType.info, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(stream, LogType.info, caller_filename, caller_function, str(data))
    return

def warning(msg, data = None):
    caller_filename = "--unknown--"
    stack = inspect.stack()
    try:
        frame = stack[1]
        module = inspect.getmodule(frame[0])
        caller_filename = module.__file__
    except:
        pass

    caller_function = "--unknown--"
    try:           
        the_class = stack[1][0].f_locals["self"].__class__
        the_method = stack[1][0].f_code.co_name
        caller_function = the_class + "." + the_method
    except:
        try:    
            caller_function = inspect.getouterframes(inspect.currentframe(), 2)[1][3]
        except:
            pass

    stream = sys.stdout
    _log_line(stream, LogType.warning, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(stream, LogType.warning, caller_filename, caller_function, str(data))
    return

def error(msg, data = None):
    caller_filename = "--unknown--"
    stack = inspect.stack()
    try:
        frame = stack[1]
        module = inspect.getmodule(frame[0])
        caller_filename = module.__file__
    except:
        pass

    caller_function = "--unknown--"
    try:           
        the_class = stack[1][0].f_locals["self"].__class__
        the_method = stack[1][0].f_code.co_name
        caller_function = the_class + "." + the_method
    except:
        try:    
            caller_function = inspect.getouterframes(inspect.currentframe(), 2)[1][3]
        except:
            pass

    stream = sys.stderr
    _log_line(stream, LogType.error, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(stream, LogType.error, caller_filename, caller_function, str(data))
    return

def fatal(msg, data = None):
    caller_filename = "--unknown--"
    stack = inspect.stack()
    try:
        frame = stack[1]
        module = inspect.getmodule(frame[0])
        caller_filename = module.__file__
    except:
        pass

    caller_function = "--unknown--"
    try:           
        the_class = stack[1][0].f_locals["self"].__class__
        the_method = stack[1][0].f_code.co_name
        caller_function = the_class + "." + the_method
    except:
        try:    
            caller_function = inspect.getouterframes(inspect.currentframe(), 2)[1][3]
        except:
            pass

    stream = sys.stderr
    _log_line(stream, LogType.fatal, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(stream, LogType.fatal, caller_filename, caller_function, str(data))
    return

class LogType(enum.Enum):
    debug = 0
    info = 1
    warning = 2
    error = 3
    fatal = 4