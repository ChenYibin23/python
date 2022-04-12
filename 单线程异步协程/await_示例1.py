import asyncio


async def func():
    print("这是第一个")

    # 将在await过程中运行获得到的值赋值给response
    response = await asyncio.sleep(2)
    # await运行结束之后运行的命令
    print('这是第二个', response)


asyncio.run(func())











