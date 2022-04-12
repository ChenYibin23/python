from greenlet import greenlet
# from flask import Flask
# app = Flask(__name__)


def func1():
    # 第一步
    print(1)
    # 第二步跳转到func2函数进行执行
    gr2.switch()
    # 第五步
    print(2)
    # 第六步跳转回func2函数进行执行
    gr2.switch()


def func2():
    # 第三步
    print(3)
    # 第四步跳转回func1函数进行执行
    gr1.switch()
    # 第五步
    print(4)


# 对greenlet进行调用，并且传入func1与func2
gr1 = greenlet(func1)
gr2 = greenlet(func2)


# 执行func1的函数
gr1.switch()
