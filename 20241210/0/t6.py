import asyncio

evsnd = asyncio.Event()
evmid0 = asyncio.Event()
evmid1 = asyncio.Event()


async def snd():
    evsnd.set()

async def mid(k):
    await evsnd.wait()
    if k:
        evmid1.set()
    else:
        evmid0.set()

async def rcv():
    await evmid0.wait()
    await evmid1.wait()

async def main():
    res = asyncio.gather(rcv(), mid(1), mid(0), snd())

asyncio.run(main())