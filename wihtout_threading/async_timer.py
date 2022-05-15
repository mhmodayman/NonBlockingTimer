import asyncio
import time


class AsyncNonBlockingTimer:
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
            yield self.timeout - ((self.loop.time() - self.start) % self.timeout)

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
