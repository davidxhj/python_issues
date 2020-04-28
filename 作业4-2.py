# 求1~100之间能被7整除，但不能同时被5整除的所有整数
count = 0
while count < 100:
    count += 1
    if count % 7 == 0 and count % 5 != 0:
        print(count)

# 求200以内能被17整除的最大正整数。
a = 0
num = 0
while num <= 200:
    num += 1
    if num % 17 == 0:
        a = num
print("a", a)

# 输出“水仙花数”。所谓水仙花数是指1个3位的十进制数，其各位数字的立方和等于该数本身。
for x in (100, 1000, 1):
    a = x % 10
    b = int(x % 100 / 10)
    c = int(x % 100)
    if x == a ^ 3 + b ^ 3 + c ^ 3:
        x = a + 10 * b + 100 * c
    print("x", x)

# 求两个整数的最大公约数.
num1 = int(input("请输入整数1："))
num2 = int(input("请输入整数2："))
if num1 > num2:
    smaller = num2
else:
    smaller = num1
for i in range(1,smaller + 1):
    if (num1 % i == 0) and (num2 % i == 0):
        number = i
print(num1, "和", num2, "的最大公约数是： ", number)

# 编写程序，输出1~1000之间能被7整除但不能同时被5整除的所有整数.
count = 0
counting = []
while count < 1000:
    count += 1
    if (count % 7 == 0) and (count % 5 != 0):
        counting.append(count)
print(counting)

# 计算π的值。利用下列公式计算π的近似值，直到最后一项的绝对值小于10^-5为止。
pi = 0
n = 1
f = 1
while n < 10000000:
    pi += f/n
    n += 2
    f = -f
print("pi = ", pi*4)