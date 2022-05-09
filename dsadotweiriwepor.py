import asyncio


class NonBlockingTimers:
    def __init__(self):
        self.loop = asyncio.new_event_loop()
        self.start = self.loop.time()
        self.delegate = self.loop.call_at(self.start, self.run)
        self.timers_callbacks_map = {}  # timer name: (callback, *args, interval, paused)

    def register_timer(self, name, interval, callback, *args, paused=False):
        self.timers_callbacks_map[name] = (callback, *args, interval, paused)

    def run(self):
        for timer in self.timers_callbacks_map.copy():
            if not self.timers_callbacks_map[timer][3]:
                self.timers_callbacks_map[timer][0](*self.timers_callbacks_map[timer][1])
                self.loop.call_later(self.timers_callbacks_map[timer][2] - ((self.loop.time() - self.start) % self.timers_callbacks_map[timer][2]),
                                     self.run)

    def pause_timer(self, timer):
        self.timers_callbacks_map[timer][3] = True

    def cancel_timer(self, timer):
        delegate = self.loop.call_later(1, lambda: False)
        delegate.cancel()
        del self.timers_callbacks_map[timer]


def cb(*args):
    x = args[0]
    y = args[1]
    print(f'I expire after {x+y}')


xTimers = NonBlockingTimers()
xTimers.register_timer('BT', 3, cb, (1.6, 1.4))
xTimers.register_timer('TT', 12, cb, (1.1, 0.9))
xTimers.loop.run_forever()
