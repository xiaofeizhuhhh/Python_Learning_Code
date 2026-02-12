import os
def read_conf():
    """
    读取配置
    :return:
    """
    file = open('file6', 'r+', encoding='utf8')
    text_info = file.read()
    print(text_info)
    my_dict = eval(text_info) #eval() 会无条件执行传入字符串中的任何 Python 代码
    print(type(my_dict))
    file.close()


if __name__ == '__main__':
    # read_conf()
    # os.system('rm -r dir4') #递归删除目录及其所有内容
    # eval("__import__('os').system('ls')")  #不要用eval执行前端发过来的任何子串，高危代码，不要执行
    pass