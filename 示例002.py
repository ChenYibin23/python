# a = "This"
# b = "is"
# c = "world"
# d = a * 3
# print(r'\t', d, '\n', d)
# a, b, c = 1, 2, 3
# print(a)
# print(b)
# print(c)


# d = isinstance(111, int)
# print(d)

# 父类
# class A:
#     pass


# # 子类
# class B(A):
#     pass


# a = isinstance(A(), A)
# True
# print(a)


# b = type(B()) == A
# # False
# print(b)


# True == 1

# str = 'myworld'


# print(str)
# print(str[0:-1])
# a = type('aaa')
# print(a)


# a = chr(92)
# print(a)


# a = 'myworld'
# print(oct(111))


# var1 = 100
# if var1:
#     print("1 - if 表达式条件为 true")
#     print(var1)

# var2 = 0
# if var2:
#     print("2 - if 表达式条件为 true")
#     print(var2)
# print("Good bye!")


# age = int(input("请输入你家狗狗的年龄:"))

# print("")
# if age <= 0:
#     print("你是在逗我吧!")
# elif age == 1:
#     print("相当于 14 岁的人。")
# elif age == 2:
#     print("相当于 22 岁的人。")
# elif age > 2:
#     human = 22 + (age - 2)*5
#     print("对应人类年龄:", human)

# # 退出提示
# input("点击 enter 键退出")

# number = -1
# guess = int(input("炸弹数为:"))
# while guess != number:
#     number = int(input(""))
#     if number > guess:
#         print("请输入介于0和%d间的数" % number)
#         continue
#     elif number < guess:
#         print("请输入介于%d和100间的数" % number)
#         continue
#     else:
#         print("踩中炸弹")
# break

# flag = 1

# while (flag):
#     print('欢迎访问菜鸟教程!')

# print("Good bye!")


# list = [1, 2, 3, 4, 5, 6, 7]
# a = iter(list)
# b = next(a)
# print(b)
# c = next(a)
# print(c)


class iterator:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = iterator()
myiter = iter(myclass)


print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
