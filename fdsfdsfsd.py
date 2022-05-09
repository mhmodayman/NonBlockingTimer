import asyncio


def call_periodic(interval, callback, *args, **kwargs):
    # get loop as a kwarg or take the default one
    loop = kwargs.get('loop') or asyncio.get_event_loop()
    # record the loop's time when call_periodic was called
    start = loop.time()

    def run(handle):
        # XXX: we could record before = loop.time() and warn when callback(*args) took longer than interval
        # call callback now (possibly blocks run)
        callback(*args)
        # reschedule run at the soonest time n * interval from start
        # re-assign delegate to the new handle
        handle.delegate = loop.call_later(interval - ((loop.time() - start) % interval), run, handle)

    class PeriodicHandle:  # not extending Handle, needs a lot of arguments that make no sense here
        def __init__(self):
            self.delegate = None

        def cancel(self):
            assert isinstance(self.delegate, asyncio.Handle), 'no delegate handle to cancel'
            self.delegate.cancel()

    periodic = PeriodicHandle()  # can't pass result of loop.call_at here, it needs periodic as an arg to run
    # set the delegate to be the Handle for call_at, causes periodic.cancel() to cancel the call to run
    periodic.delegate = loop.call_at(start + interval, run, periodic)
    # return the 'wrapper'
    return periodic


if __name__ == '__main__':
    import sys
    loop = asyncio.get_event_loop()
    # print loop's time every sys.argv[1] seconds
    handle = call_periodic(float(sys.argv[1]),
                           lambda x: print('{} at {}'.format(x, loop.time()), flush=True),
                           'Hello, world!')  # arg x to lambda
    # stop the loop after 10 seconds ...
    loop.call_later(10, lambda: loop.stop())
    # ... but cancel the periodic call before that to check if cancel() works
    loop.call_later(8, lambda: handle.cancel())
    loop.run_forever()