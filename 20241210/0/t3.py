import asyncio
import time



async def squarer(n):
    return n**2


async def doubler(n):
    return 2 * n


async def main():
    x,y = eval(input())
    middle_res = await asyncio.gather(squarer(x), squarer(y))
    print(await asyncio.gather(doubler(middle_res[0]), doubler(middle_res[1])))


asyncio.run(main())