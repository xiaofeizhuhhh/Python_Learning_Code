import sys


# print(type(sys.argv))
# print(sys.argv)
def write_hello(file_path):
    """
    必须使用命令行，如：python .\7-python程序如何传参.py file7
    :param file_path:
    :return:
    """
    file = open(file_path, 'w+', encoding='utf8')
    file.write('hello')
    file.close()


if __name__ == '__main__':
    write_hello(sys.argv[1]) #argv[0]是当前脚本的名称：如：7-python程序如何传参.py
