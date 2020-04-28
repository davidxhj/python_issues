# 编写函数，接收圆得半径作为参数，返回圆的面积
import math


def circle_area(r):
    pi = math.pi
    S = str(pi * (r * r))
    return S


r = int(input("请输入半径： "))
print('\n 圆的面积为： ' + circle_area(r))


# 编写函数，接收两个整数，返回这两个数的最大公约数（辗转相除法
def gcd(a, b):
    if a < b:
        a, b = b, a
    x = a % b
    while x != 0:
        a = b
        b = x
        x = a % b
    print(b)
    return b


def main():
    num_1 = int(input("num_1: "))
    num_2 = int(input("num_2: "))
    gcd(a=num_1, b=num_2)


if __name__ == '__main__':
    main()


# 编写函数，接收一个三位数，返回是否水仙花数。所谓水仙花数是指1个3位的十进制数，其各位数字的立方和等于该数本身
def narcissistic_num(x, y, z):
    if x ** 3 + y ** 3 + z ** 3 == 100 * z + 10 * y + x:
        print("该数是水仙花数")
    else:
        print("该数不是水仙花数")


def main():
    number0 = int(input("三位整数： "))
    x = int(number0 % 10)
    y = int(number0 / 10 % 10)
    z = int(number0 / 100)
    narcissistic_num(x, y, z)


if __name__ == '__main__':
    main()


# 编写函数，接收参数a和n，计算并返回形式如 a + aa + aaa + aaaa + … + aaa…aaa的表达式前n项的值，其中a为小于10的自然数
def Sum(a, n):
    Tn = int(0)
    Sn = []  # 初始化数列Sn
    for i in range(n):
        Tn = Tn + a
        print("数字叠加后值为: ", Tn)
        a = a * 10
        Sn.append(Tn)
        print("创建的数列为: ", Sn)
    return Sum(Sn)


print(Sum(3, 3))


# 编写函数，接收一个字符串，判断该字符串是否为回文。所谓回文是指，从前向后读和从后向前读是一样的
def judge_f(a):
    b = reversed(list(a))
    if list(b) == list(a):
        print("该字符串是回文")
    else:
        print("该字符串不是回文")
    return


a = input("请输入字符串: ")
judge_f(a)


# 写出下列程序的运行结果
def Sum(a, b=3, c=5):
    return sum([a, b, c])


print(Sum(a=8, c=2))
print(Sum(8))
print(Sum(8, 2))

"""
13
16
15
"""


# 有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少
def function(month):
    if month.isdigit():
        month = int(month)
        a = 0
        b = 1
        for i in range(month - 1):
            a, b = b, a + b
        print("%d月份以后兔子有%d对" % (month, b))
    else:
        print("输入有误请重新输入")


month = input("请输入月份:")
function(month)
