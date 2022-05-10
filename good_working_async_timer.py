import asyncio
import time


class NonBlockingTimer:
    def __init__(self, event_loop, timeout, callback, *args, shots, blocking=False):
        self.loop = event_loop
        self.start = self.loop.time()
        self.__paused = False
        self.timeout = timeout
        self.callback = callback
        self.args = args
        self.shots = shots
        self.blocking = blocking
        self.timeout_ticks_generator = self.non_drifting_ticks()
        self.task = None
        self.create_task()

    def create_task(self):
        if self.shots == 'ONE_SHOT':
            if self.blocking:
                self.task = self.loop.create_task(self.run_one_shot_blocking())
            elif not self.blocking:
                self.task = self.loop.create_task(self.run_one_shot_nonblocking())
        elif self.shots == 'PERIODIC':
            self.task = self.loop.create_task(self.run_periodic_nonblocking())

    def non_drifting_ticks(self):
        while True:
            yield self.timeout - ((loop.time() - self.start) % self.timeout)

    async def run_one_shot_blocking(self):
        if not self.__paused:
            time.sleep(next(self.timeout_ticks_generator))
            self.callback(*self.args)
            self.cancel()

    async def run_one_shot_nonblocking(self):
        if not self.__paused:
            await asyncio.sleep(next(self.timeout_ticks_generator))
            self.callback(*self.args)
            self.cancel()

    async def run_periodic_nonblocking(self):
        while not self.__paused:
            await asyncio.sleep(next(self.timeout_ticks_generator))
            self.callback(*self.args)

    def pause(self):
        self.__paused = True

    def resume(self):
        self.__paused = False

    def cancel(self):
        self.task.cancel()


def cb(*args):
    global loop
    x = args[0]
    y = args[1]
    z = args[2]
    print(f'Current time {loop.time()} and current cb is {z} and expires after {x+y}')


loop = asyncio.new_event_loop()
print(f'loop beginning time {loop.time()}')
T1 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T1-NONBLOCKING-PERIODIC', shots='PERIODIC')
T2 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T2-NONBLOCKING-PERIODIC', shots='PERIODIC')
T3 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T3-NONBLOCKING-PERIODIC', shots='PERIODIC')
T4 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T4-NONBLOCKING-PERIODIC', shots='PERIODIC')
T5 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T5-NONBLOCKING-PERIODIC', shots='PERIODIC')
T6 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T6-NONBLOCKING-PERIODIC', shots='PERIODIC')
T7 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T7-NONBLOCKING-PERIODIC', shots='PERIODIC')
T8 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T8-NONBLOCKING-PERIODIC', shots='PERIODIC')
T9 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T9-NONBLOCKING-PERIODIC', shots='PERIODIC')
T10 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T10-NONBLOCKING-PERIODIC', shots='PERIODIC')
T11 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T11-NONBLOCKING-PERIODIC', shots='PERIODIC')
T12 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T12-NONBLOCKING-PERIODIC', shots='PERIODIC')
T13 = NonBlockingTimer(loop, 7, cb, 2, 5, 'T13-NONBLOCKING-PERIODIC', shots='PERIODIC')
T14 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T14-BLOCKING-ONESHOT', shots='ONE_SHOT', blocking=True)
T15 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T15-BLOCKING-ONESHOT', shots='ONE_SHOT', blocking=True)
T16 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T16-NONBLOCKING-ONESHOT', shots='ONE_SHOT')
T17 = NonBlockingTimer(loop, 3, cb, 1, 2, 'T12-NONBLOCKING-ONESHOT', shots='ONE_SHOT')
loop.run_forever()
loop.close()
