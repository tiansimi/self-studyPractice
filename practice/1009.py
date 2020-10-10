# 冒泡排序
a = [1, 3, 10, 9, 21, 35, 4, 6]
s = range(1, len(a))[::-1]
print(type(s))
print("未交换前：%s" % a)

for i in s:
    for j in range(i):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
    print("%s轮交换后:%s" % ((len(s) - i + 1), a))
