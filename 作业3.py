# 编写程序，随机生成50个介于[1,20]之间的整数，然后统计每个整数出现频率，并输出结果

import random

# 创建50个随机整数
list_1 = []
for i in range(50):
    list_1.append(random.randint(1, 21))
print("生成50个随机整数： ", list_1)
# 计算每个数出现频率
for i in range(21):
    list_2 = []
    list_2.append(list_1.count(i))
    list_3 = set(list_2)
    print('其中元素%s出现的次数为:' % i, list_3)

# 编写程序，生成包含20个随机数的列表，将前10个元素升序排列，后10个元素降序排列，并输出结果
import random
list_4 = []
for i in range(20):
    list_4.append(random.randrange(20))
a = list_4[:11]
b = list_4[11:]
a.sort()
b.sort(reverse=True)
list_4 = a + b
print(list_4)

# 编写程序，生成一个包含20个随机整数的列表，然后对其中偶数下标的元素进行降序排列，奇数下标的元素不变
import random
list_5 = []
for i in range(20):
    list_5.append(random.randrange(20))
print("生成数列： ", list_5)
a = list_5[::2]
a.sort()
a.reverse()
list_5[::2] = a
print("排序后数列: ", list_5)

# 编写程序，让用户在键盘上输入一个包含若干整数的列表，输出翻转后的列表
list_6 = []
for i in range(20):
    list_6.append(input("请输入列表： "))
print("创建的列表为： ", list_6)
list_6.reverse()
print("翻转后的列表为：", list_6)