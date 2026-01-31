def use_hex():
    a = 123
    print(bin(a))  # 功能 将整数转换为二进制
    print(hex(a))  # 功能 将整数转换为十六进制
    print(oct(a))  # 功能 将整数转换为八进制

    b = -5

    print(bin(b))


def use_float():
    f = 1.234567891234567891    #float只有17位，int表示范围是无穷大
    print(f)


def use_bool():
    print(True + 1) #True表示1
    print(False + 1)    #False表示0


def use_complex():
    """
    python中的复数类型
    :return:
    """
    c = complex(3, 4)
    print("c is %d+%dj" % (c.real, c.imag))


# use_hex()
# use_float()
# use_bool()
use_complex()
