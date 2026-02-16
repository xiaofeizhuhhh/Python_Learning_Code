def print_info(name, title="", gender=True): #title 和 gender 都是缺省参数
    """
    name: 班上同学的姓名，是必需参数
    title: 职位，默认为空字符串
    gender: True 男生 False 女生，默认值为 True
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s%s是%s" % (title, name, gender_text))


# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值！
print_info("小明")
print_info("老王", title="班长")
print_info("小美", '学习委员',False)
print('-'*50)
#以下写法也可以，可以调换关键字参数，但是位置参数 name 必须在缺省参数 title 和 gender 后面
print_info("小美", gender=False,title='学习委员')

