def aaa(x):
    # 函数内定义全局变量
    global bbb
    bbb = 1000
    ccc = x + bbb
    print(ccc)


def ddd(x):
    ppp = x * bbb
    print(ppp)


# 调用函数
aaa(10)
ddd(10)
