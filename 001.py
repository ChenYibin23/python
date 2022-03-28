# 这是注释
# a = 1

# print(a)


# def get_sum(sum1, sum2):
#     result = sum1 + sum2
#     return result


#a = 1
# b = 2
# c = get_sum(a, b)
# print(a)
# 返回result的值


# import turtle
# from sqlalchemy import true


# list1 = [1, 3, 2, 4, 5]
# 降第1个元素修改成9
# list1[1] = 9
# 添加一个元素6
# list1.append(6)
# 删除第0个元素
# list1.pop(0)
# 删除指定的元素 3
# list1.remove(3)
# 在第0个元素前添加上元素0
# list1.insert(0, 0)
# 使列表按照由小到大排列
# list1.sort()
# 使列表按照由大到小排列
# list1.reverse()
# 使用索引置顶数组中第2个元素
# print(list1.index(2))

# print(list1)


# tuple1 = (1, 2, 3)
# 显示元组中的第一个元素
# print(tuple1[0])
# 元组与列表的相互转化
# list2 = list(tuple1)
# tuple2 = tuple(list1)
# print(tuple1)


# dict1 = {"name": "老张", "height": 170, "weight": 100}
# # 输出字典中的name键的值
# print(dict1["name"])
# # 输出字典的长度(键的个数)
# print(len(dict1))
# # 获得字典dict中所有的键
# print(dict1.keys())
# # 获得字典中所有的值
# print(dict1.values())
# # 修改字典中name的值为老王
# dict1["name"] = "老王"
# # 在字典末尾添加键值gender
# dict1["gender"] = "男"
# # 删除字典中的键值name
# dict1.pop("name")

# print(dict1)

# 集合会自动排序
# 集合中不会存在重复元素
# 创建集合的两种方式
# 集合并没有顺序概念

# set1 = set((1, 2, 4, 3, 5))
# from turtle import pensize

# from sqlalchemy import false
# set1 = {1, 2, 3, 4, 5}
# 删除集合中的元素3
# # set1.discard(3)
# set2 = {4, 5, 6}
# # 输出集合set1与集合set2中共有的元素
# print(set1.intersection(set2))
# # 输出集合set1中有但集合2中没有的元素
# print(set1.difference(set2))
# # 输出集合set2中有但集合set1中没有的元素
# print(set2.difference(set1))
# # 如果集合set2是集合set1的子集的话输出Ture，否则输出False
# print(set2.issubset(set1))
# # print(set1)


# homework_finished = True

# if (homework_finished):
#     print("A")
# else:
#     print("B")


# prize = 1000
# 如果满足就返回Ture，不满足就返回Flase
# expensive = (prize > 800)

# print(expensive)

# size = 1000

# if (size > 800):
#     print("A")
# elif (size > 600):
#     print("B")
# elif (size > 400):
#     print("c")
# elif (size > 200):
#     print("D")
# else:
#     print("f")

# a = 10
# while (a > 5):
#     print(a)
#     a -= 1
# print("循环结束")
# # for可以对字符串，列表，元组进行遍历
# string1 = "dhauigbah"

# for aaa in string1:
#     print(aaa)

# list1 = ["老邓", "老张", "老王"]

# for aaa in list1:
#     print(aaa)

# range(初始,结尾,步距)创建一个序列
# 结尾的数并不会输出
# 默认情况下开始为0，步距为1
# for i in range(0, len(list1), 1):
#     print(i)

# # 获取list1中的元素
# for i in range(0, len(list1), 1):
#     print(list1[i])

# # break：直接结束循环

# for i in range(10):
#     print(i)
#     if(i == 5):
#         break

# print("循环结束")

# aaa = [False, True, False, True]
# # continue：跳过后面的内容进行下一次循环
# for bbb in aaa:

#     if(bbb):
#         continue

# print("科比·布莱恩特")
