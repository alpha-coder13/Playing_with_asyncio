import asyncio
import time
from asyncio import tasks

from asyncio.tasks import  sleep

async def multiply(A,B):
    print("entering couroutine of {} \n".format(B))
    val=[] 
    for k in range(A+1):
        if k % B ==0:
            val.append(k)
        if k % 5000 == 0:
            await sleep(0.01)
    print("Exiting the coroutine of {} \n".format(B))
async def main():
    a=time.localtime()[5]
    Task_1=asyncio.create_task(multiply(100000000,1090))
    Task_3=asyncio.create_task(multiply(50000,29))
    Task_2=asyncio.create_task(multiply(100,10))

    await Task_3
    await Task_1
    await Task_2
    b=time.localtime()[5]
    print("\n",b-a)

asyncio.run(main())
