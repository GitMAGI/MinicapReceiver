import enum
import datetime
import sys
import inspect

class Log:
    min_level = -1
    _last_line_was_overwritten = False
    _last_line_length = -1

    def _log_line(self, stream, overwrite, type, caller_filename, caller_function, data):
        try:
            if type.value < self.min_level:
                return

            current_time_str = str(datetime.datetime.now())
            type_str = type.name.capitalize()
            line = "{} | {} | {} @ {} >>> {}".format(current_time_str, type_str, caller_function, caller_filename, data)
            #line = "{}\t{}\t{}\t{}\t{}".format(current_time_str, type_str, caller_function, caller_filename, data)

            if overwrite:
                # Write a white line as long as the max between the current line and the previous one
                fake_line = ""
                for i in range(1, max(len(line), self._last_line_length + 1), 1):
                    fake_line += " "
                stream.write("\r%s" % fake_line)

                # Write a line in an overwritten mode
                stream.write("\r%s" % line)
                self._last_line_was_overwritten = True
            else:
                if self._last_line_was_overwritten:
                    stream.write("\n") 
                stream.write("%s\n" % line) 
                self._last_line_was_overwritten = False    
            stream.flush()
            
            self._last_line_length = len(line)
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
        self._log_line(stream, overwrite, LogType.debug, caller_filename, caller_function, msg)
        if data is not None:
            self._log_line(stream, overwrite, LogType.debug, caller_filename, caller_function, str(data))
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
        self._log_line(stream, overwrite, LogType.info, caller_filename, caller_function, msg)
        if data is not None:
            self._log_line(stream, overwrite, LogType.info, caller_filename, caller_function, str(data))
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
        self._log_line(stream, overwrite, LogType.warning, caller_filename, caller_function, msg)
        if data is not None:
            self._log_line(stream, overwrite, LogType.warning, caller_filename, caller_function, str(data))
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
        self._log_line(stream, overwrite, LogType.error, caller_filename, caller_function, msg)
        if data is not None:
            self._log_line(stream, overwrite, LogType.error, caller_filename, caller_function, str(data))
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
        self._log_line(stream, overwrite, LogType.fatal, caller_filename, caller_function, msg)
        if data is not None:
            self._log_line(stream, overwrite, LogType.fatal, caller_filename, caller_function, str(data))
        return

class LogType(enum.Enum):
    debug = 0
    info = 1
    warning = 2
    error = 3
    fatal = 4