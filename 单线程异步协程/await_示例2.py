import asyncio


# 创建一个协程函数
async def others():
    print('start')
    await asyncio.sleep(2)
    print('end')
    # 传回到reponse中值
    return ('response111')


async def func():
    print('运行协程函数的内部代码')

    # 将运行others得到的对象赋值给response
    response = await others()

    print('运行others获得到的值', response)


asyncio.run(func())
