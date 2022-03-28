class aaa:
    def __init__(self, name, ggg):
        print("ddddddd")
        self.name = name
        self.ggg = ggg
        # 调用__init__函数时发生的事件
        print("ffff{}eeee{}".format(self.name, ggg))

    def eating(self):
        print("aaaaaaa")

    def drinking(self):
        print("bbbbbbbb")


# 创建对象ccc
# 为__init__函数中的对象进行赋值
# __init__函数不需要调用也能运行
# __init__是类的构造函数。
# 就像上面提到的那样，一旦分配了对象的内存，就会调用__init__方法。
# 当我们用("大黄","111")调用函数__init__时，
# 它将作为参数("大黄", "111")传递给__init__函数。
# 传入的参数需要与__init__中的参数名的数量相同
# self指向的就是对象ccc，ddd
ccc = aaa("大黄", "111")
ddd = aaa("二黄", "222")

# 调用aaa中的函数eating
ccc.eating()

# 打印对象ccc的内存地址
# 地址可用于进行对象的引用
print(id(ccc))
