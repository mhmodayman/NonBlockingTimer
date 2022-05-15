import asyncio
from async_timer import AsyncNonBlockingTimer


def cb(*args):
    global loop
    x = args[0]
    y = args[1]
    z = args[2]
    print(f'Current time {loop.time()} and current cb is {z} and expires after {x+y}')


loop = asyncio.new_event_loop()
print(f'loop beginning time {loop.time()}')
T1 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T1-NONBLOCKING-PERIODIC', shots='PERIODIC')
T2 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T2-NONBLOCKING-PERIODIC', shots='PERIODIC')
T3 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T3-NONBLOCKING-PERIODIC', shots='PERIODIC')
T4 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T4-NONBLOCKING-PERIODIC', shots='PERIODIC')
T5 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T5-NONBLOCKING-PERIODIC', shots='PERIODIC')
T6 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T6-NONBLOCKING-PERIODIC', shots='PERIODIC')
T7 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T7-NONBLOCKING-PERIODIC', shots='PERIODIC')
T8 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T8-NONBLOCKING-PERIODIC', shots='PERIODIC')
T9 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T9-NONBLOCKING-PERIODIC', shots='PERIODIC')
T10 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T10-NONBLOCKING-PERIODIC', shots='PERIODIC')
T11 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T11-NONBLOCKING-PERIODIC', shots='PERIODIC')
T12 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T12-NONBLOCKING-PERIODIC', shots='PERIODIC')
T13 = AsyncNonBlockingTimer(loop, 7, cb, 2, 5, 'T13-NONBLOCKING-PERIODIC', shots='PERIODIC')
T14 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T14-BLOCKING-ONESHOT', shots='ONE_SHOT', blocking=True)
T15 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T15-BLOCKING-ONESHOT', shots='ONE_SHOT', blocking=True)
T16 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T16-NONBLOCKING-ONESHOT', shots='ONE_SHOT')
T17 = AsyncNonBlockingTimer(loop, 3, cb, 1, 2, 'T12-NONBLOCKING-ONESHOT', shots='ONE_SHOT')
loop.run_forever()
loop.close()
