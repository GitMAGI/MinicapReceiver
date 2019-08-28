import time
import sys

def elapsed_time_string(elapsed_time):
    millis = int(round(elapsed_time * 1000))
    return time.strftime("%H:%M:%S", time.gmtime(elapsed_time)) + str(".%03d" % millis)

def print_progress_bar(value, endvalue, bar_length=20):
    percent = float(value) / endvalue
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()
    
    if value == endvalue:
        sys.stdout.write('\n')