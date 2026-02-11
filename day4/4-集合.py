def use_set():
    set1 = set()  # 定义一个空集合
    print(type(set1))

    set2 = {1, 2, 3, 4, 5}  # 不支持随机访问

    fruits = {"apple", "banana", "cherry"}
    fruits.add("orange")    #位置是乱放的
    print(fruits)

    fruits = {"apple", "banana", "cherry"}
    x = fruits.copy()
    print(id(x))    #集合是可变数据类型，所以复制后id不一样
    print(id(fruits))

    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    z = x.difference(y)
    print(f'差集{z}')

    x = {"apple", "banana", "cherry"}
    y = {"google", "microsoft", "apple"}
    x.difference_update(y)
    print(x)
    print('-' * 50)
    fruits = {"apple", "banana", "cherry"}
    fruits.discard("banana")
    print(fruits)
    print('-' * 50)
    x = {"a", "b", "c"}
    y = {"c", "d", "e"}
    z = {"f", "g", "c"}
    result = x.intersection(y, z)
    print(result)
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.symmetric_difference(y)
    print(z)
    print('-' * 50)
    x = {"apple", "banana", "cherry"}
    y = {"google", "runoob", "apple"}
    z = x.union(y)
    print(z)

    print('apple' in z) #判断元素是否在集合中

    print(x - y)
    print(x | y)
    print(x & y)
    print(x ^ y) #求对称差集，返回新集合


def use_generator():
    """
    使用生成式
    :return:
    """
    my_tuple = tuple(x for x in range(10))  # 生成器表达式 + tuple()
    print(my_tuple)
    my_set = {x for x in 'abracadabra' if x not in 'abc'}
    print(my_set)
    print(len(my_set))


if __name__ == '__main__':
    use_set()
    use_generator()
    t = tuple([x for x in range(5)]) #列表生成式 + tuple()
    print(t)  # (0, 1, 2, 3, 4)
    t = tuple(range(5)) #直接传可迭代对象
    print(t)  # (0, 1, 2, 3, 4)