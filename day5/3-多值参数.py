# 多值参数，就是参数个数不确定，必须是下面的写法

def demo2(*args, **kwargs): #*args收集元素作为元组，**kwargs收集元素作为字典
    print(f'demo2-{args}')
    print(f'demo2-{kwargs}')


def demo(*args, **kwargs):
    # print(num)
    print(args)
    print(kwargs)
    demo2(*args,**kwargs)

# demo2(1,2)
demo(1, 2, 3, 4, name='小明', age=19)