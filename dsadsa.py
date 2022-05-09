import time
import asyncio
import abc


class PeriodicAsyncThread:
    def __init__(self, period):
        self.period = period

    def periodic(self):
        def scheduler(fcn):
            async def wrapper(*args, **kwargs):
                def g_tick():
                    t = time.time()
                    count = 0
                    while True:
                        count += 1
                        yield max(t + count * self.period - time.time(), 0)
                g = g_tick()

                while True:
                    # print('periodic', time.time())
                    asyncio.create_task(fcn(*args, **kwargs))
                    await asyncio.sleep(next(g))
            return wrapper
        return scheduler

    @abc.abstractmethod
    async def run(self, *args, **kwargs):
        return

    def start(self):
        asyncio.run(self.run())


class APeriodicThread(PeriodicAsyncThread):
    def __init__(self, period):
        super().__init__(period)
        self.run = self.periodic()(self.run)

    async def run(self, *args, **kwargs):
        await asyncio.sleep(2)
        print(time.time())


apt = APeriodicThread(2)
apt.start()


for i in range(10):
    print(i)

print(44444444444444)

print('ppppppppppppppppppppp')

while True:
    time.sleep(4)
    break

print('finished')
