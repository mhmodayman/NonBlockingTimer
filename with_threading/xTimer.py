import threading
import time

__author__ = "ICP(ivanhaleh@gmail.com)"
__date__ = "$02-may-2012 17:12:56$"


class XTimer:
    def __init__(self, timeout, callback, *args, shots_num=-1):
        """
        (shots_num < 0) --> periodic timer
        """

        self.thread = None
        self.state = None
        self.timeout = timeout
        self.callback = callback
        self.args = args
        self.shots_num = shots_num
        self.shots_counter = 0
        self.state = "initializing"

    def pause(self):
        self.state = "paused"

    def terminate(self):
        self.state = "terminated"
        del self.thread
        del self

    def start(self):
        if self.state == "initializing":
            self.state = "running"
            self.thread = threading.Thread(target=self.main_loop, args=())
            self.thread.start()
        elif self.state == "paused":
            self.state = "running"

    def main_loop(self):
        while True:
            if self.state == "running":
                time.sleep(self.timeout)
                if self.state == "running":
                    self.callback(*self.args)
                    self.shots_counter += 1
                    if 0 < self.shots_num <= self.shots_counter:
                        self.shots_counter = 0
                        self.state = "terminated"
            elif self.state == "terminated":
                self.terminate()
                break
            elif self.state == "paused":
                pass
