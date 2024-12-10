import asyncio

async def prod(queue):
    for i in range(5):
        await queue.put(f'value_{i}')
        print(f'prod: put {i} to q1')
        await asyncio.sleep(1)

async def mid(q1, q2):
    while True:
        res = await q1.get()
        print(f'mid: got {res} from q1')
        await q2.put(res)
        print(f'mid: put {res} to q2')


async def cons(q2):
    while True:
        res = await q2.get()
        print(f'cons: got {res} from q2')

async def main():
    q1 = asyncio.Queue()
    q2 = asyncio.Queue()
    ptask = asyncio.create_task(prod(q1))
    mtask = asyncio.create_task(mid(q1, q2))
    ctask = asyncio.create_task(cons(q2))

    await ptask
    mtask.cancel()
    ctask.cancel()


    '''await asyncio.gather(
        prod(q1),
        mid(q1, q2),
        cons(q2)
    )'''

asyncio.run(main())