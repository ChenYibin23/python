import asyncio


# 该函数中的await并不会切换到其他线程，只会进行延时
async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return '返回值'


async def func1():
    # await asyncio.sleep(1)
    print(3)
    await asyncio.sleep(3)
    print(4)
    return "返回值"


async def main():
    print('start')
    # 创建sr1和sr2两个task对象，并将该任务添加到事件循环当中
    # 此处的事件是运行func()函数
    # 添加的顺序就是执行时的顺序
    # sr1与sr2都代表这个task列表，都可以进行循环，但是进行await的会优先运行
    # 优先运行则是主线程，当主线程运行结束之后其他线程全部停止运行
    sr1 = asyncio.create_task(func())
    sr2 = asyncio.create_task(func1())

    print(sr1)
    print(sr2)
    print('end')

    # 此处执行sr1，运行func函数，等同于 await func()
    # 此处await的是主线程
    # 当主线程结束之后全部异步线程不再运行
    ret1 = await sr1
    # ret2 = await sr2
    # print(ret1, ret2)
    print(ret1)
# 先执行func函数之后遇到await之后同步执行func1，所以两次打印1的时间极短，之后func()与func1()中的sleep(2)同步执行
# 输出的结果是
# start
# end
# 1
# 1
# 2
# 3
# 返回值 返回值


# 运行main()函数
asyncio.run(main())
