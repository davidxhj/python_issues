# 编写函数，提示用户输入一个字符串，然后输出该字符串是否回文串
def judge_f(a):
    b = reversed(list(a))
    if list(b) == list(a):
        print("该字符串是回文")
    else:
        print("该字符串不是回文")
    return


a = input("请输入字符串: ")
judge_f(a)


# 编写函数，提示用户输入一个字符串，然后显示字符串中字母出现的次数
def num_count(s):
    ca = 0
    cn = 0
    for s1 in s:
        if s1.isalpha():
            ca += 1
        if s1.isdigit():
            cn += 1
    print(ca)
    return


s = str(input("请输入字符串： "))
num_count(s)


# 编写函数，将十六进制数转换为十进制数
def hex_dec(a):
    a.lower()
    print(int(a, 16))


a = input("请输入16进制: ")
hex_dec(a)