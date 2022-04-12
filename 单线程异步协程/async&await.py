import asyncio

async def func1():
    print(1)
    # 网络IO请求：下载一张图片
    await asyncio.sleep(2)
    # 当遇到IO的耗时操作时自动切回tasks中的其他任务
    print(2)


async def func2():
    print(3)
    # 网络IO请求：下载一张图片
    await asyncio.sleep(2)
    # 当遇到IO的耗时操作时自动切回tasks中的其他任务
    print(4)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]


loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))