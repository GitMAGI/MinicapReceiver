import enum
import datetime
import sys
import inspect

class Log:
    __min_level = -1
    __last_line_was_overwritten = False
    __last_line_length = -1

    # Here will be the instance stored.
    __instance = None

    def __init__(self):
        self.__min_level = -1
        self.__last_line_was_overwritten = False
        self.__last_line_length = -1

        if Log.__instance != None:
            raise Exception("This class is a singleton! Call get_instance method instead!")
        else:
            Log.__instance = self

    @staticmethod
    def set_min_level(level):
        """ Static access method. """
        if Log.__instance == None:
            Log()            
        Log.__instance.__min_level = level

    @staticmethod
    def get_instance():
        """ Static access method. """
        if Log.__instance == None:
            Log()
        return Log.__instance 

    def __log_line(self, stream, overwrite, type, caller_filename, caller_function, data):
        try:
            if type.value < self.__min_level:
                return

            current_time_str = str(datetime.datetime.now())
            type_str = type.name.capitalize()
            line = "{} | {} | {} @ {} >>> {}".format(current_time_str, type_str, caller_function, caller_filename, data)
            #line = "{}\t{}\t{}\t{}\t{}".format(current_time_str, type_str, caller_function, caller_filename, data)

            if not overwrite:
                if self.__last_line_was_overwritten:
                    stream.write("\n") 

                self.__last_line_was_overwritten = False
                stream.write("%s\r\n" % line) 
            else:
                # Write a white line as long as the max between the current line and the previous one
                fake_line = ""
                for i in range(1, max(len(line), self.__last_line_length + 1), 1):
                    fake_line += " "
                stream.write("%s\r" % fake_line)

                # Write a line in an overwritten mode
                self.__last_line_was_overwritten = True
                stream.write("%s\r" % line)
            
            stream.flush()
            
            self.__last_line_length = len(line)
        except Exception as e:
            print(str(e))
            sys.stderr.write("Erorr during the log operation\n")
            sys.stderr.flush()
        return

    def debug(self, msg, data = None, overwrite = False):
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
        self.__log_line(stream, overwrite, LogType.debug, caller_filename, caller_function, msg)
        if data is not None:
            self.__log_line(stream, overwrite, LogType.debug, caller_filename, caller_function, str(data))
        return

    def info(self, msg, data = None, overwrite = False):
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
        self.__log_line(stream, overwrite, LogType.info, caller_filename, caller_function, msg)
        if data is not None:
            self.__log_line(stream, overwrite, LogType.info, caller_filename, caller_function, str(data))
        return

    def warning(self, msg, data = None, overwrite = False):
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
        self.__log_line(stream, overwrite, LogType.warning, caller_filename, caller_function, msg)
        if data is not None:
            self.__log_line(stream, overwrite, LogType.warning, caller_filename, caller_function, str(data))
        return

    def error(self, msg, data = None, overwrite = False):
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
        self.__log_line(stream, overwrite, LogType.error, caller_filename, caller_function, msg)
        if data is not None:
            self.__log_line(stream, overwrite, LogType.error, caller_filename, caller_function, str(data))
        return

    def fatal(self, msg, data = None, overwrite = False):
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
        self.__log_line(stream, overwrite, LogType.fatal, caller_filename, caller_function, msg)
        if data is not None:
            self.__log_line(stream, overwrite, LogType.fatal, caller_filename, caller_function, str(data))
        return

class LogType(enum.Enum):
    debug = 0
    info = 1
    warning = 2
    error = 3
    fatal = 4