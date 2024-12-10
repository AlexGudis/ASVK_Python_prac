import asyncio

async def squarer(n):
    return n**2


async def doubler(n):
    return 2 * n


async def main():
    x,y = eval(input())
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(squarer(x))
        task2 = tg.create_task(squarer(y))
        check1 = task1.result()
        check2 = task2.result()
        print(f'CHECK1 = {check1}')
        print(f'CHECK2 = {check2}')
        task3 = tg.create_task(squarer(task1.result()))
        task4 = tg.create_task(squarer(task2.result()))
    print(f"Both tasks have completed now: {task3.result()}, {task4.result()}")
    return 0

asyncio.run(main())