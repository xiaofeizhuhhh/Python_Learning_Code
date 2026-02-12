class MusicPlayer(object):
    instance = None  # 用来存储唯一的实例对象

    def __new__(cls, *args, **kwargs):
        # 1、创建对象，分配空间
        if cls.instance is None: #确保无论实例化多少次，都返回同一个对象
            cls.instance=super().__new__(cls)  #父亲的new类似于C的malloc
        return cls.instance

    def __init__(self,name):
        self.name=name

if __name__ == '__main__':
    player1 = MusicPlayer('七里香')
    player2 = MusicPlayer('东风破')
    print(id(player1))
    print(id(player2)) # 打印两个对象的id，可以看到是同一个对象
    print(player1.name)
    print(player2.name)