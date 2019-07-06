import enum
import datetime
import sys
import inspect

def _log_line(type, caller_filename, caller_function, data):
    try:
        current_time_str = str(datetime.datetime.now())
        type_str = type.name.capitalize()
        line = "{} | {} | {} @ {} >>> {}".format(current_time_str, type_str, caller_function, caller_filename, data)
        print("{}".format(line))
    except:
        print("Erorr during the log operation")
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

    _log_line(LogType.debug, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(LogType.debug, caller_filename, caller_function, str(data))
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

    _log_line(LogType.info, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(LogType.info, caller_filename, caller_function, str(data))
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

    _log_line(LogType.warning, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(LogType.warning, caller_filename, caller_function, str(data))
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

    _log_line(LogType.error, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(LogType.error, caller_filename, caller_function, str(data))
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

    _log_line(LogType.fatal, caller_filename, caller_function, msg)
    if data is not None:
        _log_line(LogType.fatal, caller_filename, caller_function, str(data))
    return

class LogType(enum.Enum):
    debug = 0
    info = 1
    warning = 2
    error = 3
    fatal = 4