import asyncio


# 创建一个协程函数
async def others():
    print("start")
    # 运行一个await语句，进行一个IO等待
    await asyncio.sleep(2)
    print("end")
    # 将结果返回到协程对象当中
    return ('返回值')


async def func():
    print('运行协程函数内部代码')
    # others()是协程对象
    # 将await过程中获得值赋值给response1，也就是start -(2s)-> end
    # 在await过程中执行协程函数others
    # 没有添加在task列表中的任务会顺序执行并不会切换线程
    response1 = await others()
    print('IO请求结束，结果为：', response1)

    response2 = await others()
    print('IO请求结束，结果为：', response2)

# 运行协程对象func()
asyncio.run(func())





