class A:
    def test(self):
        print('A test')

    def demo(self):
        print('A demo')


class B:
    def test(self):
        print('B test')

    def demo(self):
        print('B demo')


class C(A, B):
    def test(self):
        print('C test')


if __name__ == '__main__':
    c = C()
    c.test()
    print(C.__mro__)



    # 更优雅的方式：所有类都使用 super()
    class Base1:
        def __init__(self):
            super().__init__()
            print("Base1 init")


    class Base2:
        def __init__(self):
            super().__init__()
            print("Base2 init")


    class Sub(Base1, Base2):
        def __init__(self):
            super().__init__()
            print("Sub init")

    # 调用顺序：Base2.init → Base1.init → Sub.init (因为 MRO 顺序)
    s = Sub()