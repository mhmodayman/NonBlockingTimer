import time
import asyncio


class PeriodicAsyncThread:
    def __init__(self, period, callback, *args):
        self.period = period
        self.run = self.periodic()(callback)
        self.args = args
        self.paused = False

    def periodic(self):
        def scheduler(fcn):
            async def wrapper(*args, **kwargs):
                def g_tick():
                    print(4)
                    t = time.time()
                    count = 0
                    while True:
                        count += 1
                        yield max(t + count * self.period - time.time(), 0)

                while not self.paused:
                    print('periodic', time.time())
                    asyncio.create_task(fcn(*self.args, **kwargs))
                    await asyncio.sleep(next(g_tick()))
            return wrapper
        return scheduler

    def start(self):
        asyncio.run(self.run())

    def pause(self):
        self.paused


async def ply_ft(x):
    print('playing')
    while True:
        time.sleep(3.5)
        break


apt = PeriodicAsyncThread(3, ply_ft, 1)
apt.start()


for i in range(10):
    print(i)

print(44444444444444)

print('ppppppppppppppppppppp')

while True:
    time.sleep(4)
    break

print('finished')
