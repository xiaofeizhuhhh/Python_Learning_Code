import sys
#动态修改 Python 的模块搜索路径，将自定义目录 'module' 插入到搜索路径列表的最前面，并打印修改后的路径列表
sys.path.insert(0,'module') #将'module'目录插入到搜索路径列表的最前面，即 0 号索引位置
print(sys.path)
print('-'*50)
import my_module

my_module.test1()