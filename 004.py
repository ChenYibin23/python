# class User(object):

#     # 父级
#     def __init__(self, something):
#         print("User Init called.")
#         self.something = something

#     def method(self):
#         return self.something

#     # 子级


# class Student(User):
#     def __init__(self, something):
#         User.__init__(self, something)
#         print("Student Init called.")
#         self.something = something

#     def method(self):
#         return self.something


# #  新建对象时会触发__init__函数
# # 传入时会先调用父级再调用子级
# my_object = Student('Jetty')


# from sympy import content


import re
content = '''
01 aaaaaaaaaaaaaa
02 bbbbbbbbbbbbbbbb
03 cccccccccccccccccc
04 ddddddddddddddddd
'''

# 引用re模块
pattern = re.compile(r'前端.*')
print(pattern.findall(content))
# print(type(pattern))

for aaa in pattern.findall(content):
    print(aaa)
