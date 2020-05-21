# 计算前n个自然数的阶乘之和1!+2!+3!+...+n!的值
n = int(input())
jie = 1
sum = 0
i = 1
while n >= i:
    jie = jie * i
    sum = sum + jie
    i = i + 1
print(sum)

# 显示数字金字塔。编写程序提示用户输入一个在1到15之间的整数，然后显示一个金字塔。
n = eval(input("Enter the number of lines："))
for i in range(1, n + 1):
    a = (n - i) * ' '
    print(a, end='')
    for j in range(1, i + 1):
        print(i - j + 1, end='')
        if (i - j + 1) == 1:
            if i != 1:
                for k in range(2, i + 1):
                    print(k, end='')
    print()
