my_list = [x for x in range(10)]  # 理解：对于range(10)中的每个元素x，将x作为列表元素添加到my_list中

print(my_list)

# 2个for循环
a = [j for i in range(10) for j in range(i)]
print(a)
# 二维列表
a = [[col * row for col in range(5)] for row in range(5)]
print(a)
# print(a[1][2])
# 二维转一维
b = [j for x in a for j in x]
print(b)

# 使用if
c = [x for x in range(10) if x % 2 == 0]
print(c)

# 使用if else，必须放在for前面
d = [x if x % 2 == 0 else x ** 2 for x in range(10)]
print(d)
