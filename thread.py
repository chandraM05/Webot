# import thread
# import time

# def print_time( threadName, delay):
#    count = 0
#    while count < 5:
#       time.sleep(delay)
#       count += 1
#       print "%s: %s" % ( threadName, time.ctime(time.time()) )

# # Create two threads as follows
# try:
#    thread.start_new_thread( print_time, ("Thread-1", 2, ) )
#    thread.start_new_thread( print_time, ("Thread-2", 4, ) )
# except:
#    print "Error: unable to start thread"

# while 1:
#    pass

import threading
from threading import Thread

def func1():
    print '1 :Working'

def func2():
    print '2 :Working'

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()