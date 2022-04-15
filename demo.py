import xTimer
import time
import threading

__author__ = "ICP(ivanhalen@gmail.com)"
__date__ = "$02-may-2012 23:41:48$"


def callback1():
    print("Hello periodic timer")
    print(time.time(), "my thread %s" % str(threading.current_thread().ident), '\n')


def callback2(text_msg):
    global xT1
    print(text_msg)
    print(time.time(), "my thread %s" % str(threading.current_thread().ident), '\n')
    xT1.terminate()


if __name__ == "__main__":
    # EVERY 2 SECONDS RUNS INFINITELY
    xT1 = xTimer.XTimer(2, callback1)
    xT1.start()
    # EVERY 10 SECONDS IT RUNS ONLY 1 TIME
    xT2 = xTimer.XTimer(10, callback2, "Hello on shot timer")
    xT2.start()
