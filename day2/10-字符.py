str1 = 'a'
print(type(str1))
str2 = 'abc'
print(type(str2))

str3 = "abc'defg"
print(str3)

str4 = ('abc\nbcd') #\n表示换行
print(str4)

str5 = 'abc\'\"bcd'  # 转义字符，\'表示单引号，\"表示双引号
print(str5)

str6 = 'abc\\\\bcd' #\\表示反斜杠，一个\需要用\\表示
print(str6)

print('-' * 50) # 输出50个-
print(ord('0'))  # 字符0的整形值，使用ord()函数可以查看ASCII码
print(chr(65))  #使用chr()函数可以查看ASCII码对应的字符
