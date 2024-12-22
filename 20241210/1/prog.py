import asyncio
from collections import deque


async def writer(queue, delay, stop_event):
    counter = 0
    #print(f'writer_{delay} starts')
    while not stop_event.is_set():
        #print(f'writer_{delay} sleeps...')
        await asyncio.sleep(delay)
        #print(f'writer_{delay} works!')
        item = f"{counter}_{delay}"
        await queue.put(item)
        counter += 1

async def stacker(queue, stack, stop_event):
    while not stop_event.is_set() or not queue.empty():
        item = await queue.get()
        stack.append(item)

async def reader(stack, count, delay, event):
    await asyncio.sleep(delay)
    check = 0
    while check != count:
        while not stack:
            await asyncio.sleep(0.0001)
        item = stack.pop(0)
        print(item)
        check += 1
        await asyncio.sleep(delay)
    event.set()


async def main():
    delay1, delay2, delay3, count = eval(input())
    
    queue = asyncio.Queue()
    stack = []
    stop_event = asyncio.Event()

    tasks = [
        asyncio.create_task(writer(queue, delay1, stop_event)),
        asyncio.create_task(writer(queue, delay2, stop_event)),
        asyncio.create_task(stacker(queue, stack, stop_event)),
        asyncio.create_task(reader(stack, count, delay3, stop_event)),
    ]
    await asyncio.gather(*tasks)

asyncio.run(main())
