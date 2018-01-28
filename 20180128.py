#!/usr/bin/env python
#coding=utf-8
#每个代码块每行缩进要一样
'''
if False:
    print(11111111111);
else:
    print(22222222222);
'''
#控制台输入
'''print(input('pleas input something and end with enter key.\n'))
print('Python语句中一般以新行作为为语句的结束符。但是我们可以使用斜杠（ \）将一行的语句分为多行显示')
'''
#换行输出
'''print('contents', end='!@#$%^&*')
#end就表示print将如何结束，默认为end="\n"（换行）
print("祝各位身体健康")
print("！")
print("祝各位身体健康", end='')
print("！")'''

#变量
'''intdata = 111
floatdata = 111.1
strdata = '1111';
print(intdata)
print(floatdata)
print(strdata)
#给多个变量赋值
a=b=c=1 #赋值内容相同
d,e,f=1.1,2,3 #赋值内容不同
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
'''
#5个标准数据类型 Numbers String List Tuple Dictionary
#字符串操作
'''
str="0123456"
print(str[1])#从做往右，跟正常的位置一样
print(str[-3:-1])#从右往左，最右边是-1
print(str[:1])
print(str[5:])
print(str[5:6])
print(str*2)
print(str+"789")
'''
#列表操作(相当于java中的list)
'''
list1 = ['item1', 'item2', 'item3'];
list2 = ['item1', 'item2', 'item3'];
print(list1[-1])
print(list2*2)
print(list1+list2)
print(list1+[[1,2,3],[4,5,6]])
'''
#元组操作（相当于只读列表）
'''
tuple=('1',2,3.1)
#tuple[1]=2.1 #元组里面的元素不支持二次赋值，所以这样写是错的
tuple1=('1',2,3.1)
print(tuple[-1])
print(tuple[0])
print(tuple[1:])
print(tuple*2)
print(tuple+tuple1)
'''
#字典操作（相当于java中的map）
'''
dictionary={"1":1,2:"2",3:[1,2,3],4:(1,2,3),5:{1:1}}
print(dictionary)
print(dictionary[5])
print(dictionary.keys())
print(dictionary.values())
'''
#数据类型转换
'''
print(int(1.1))
print(1.1)
print type(bool("True"))
print type(str(111))
print type(float("111"))
print float("1111")
'''
#算术运算符 + - * / %（除取余数） **（幂运算） //（商取整数）(赋值运算符:= += -= *= /= %=（除取余数） **=（幂运算） //=（商取整数）)
'''
a=100
b=10
c=0
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**0)
print(a//b)
print("测试运算符",end="over")
'''
#比较运算符
'''
if(1==1):
    print(1==1)
if(1!=2):
  print("yibudengyuer")
'''
#位运算符
'''
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        # 12 = 0000 1100
print("1 - c 的值为：", c)

c = a | b;        # 61 = 0011 1101 
print("2 - c 的值为：", c)

c = a ^ b;        # 49 = 0011 0001
print( "3 - c 的值为：", c)

c = ~a;           # -61 = 1100 0011
print( "4 - c 的值为：", c)

c = a << 2;       # 240 = 1111 0000
print( "5 - c 的值为：", c)

c = a >> 2;       # 15 = 0000 1111
print( "6 - c 的值为：", c)
'''
#逻辑运算符 and or not
#成员运算符 in not in
'''print(2 in (1,3))'''
#身份运算符 is is not
'''
print(1 is 2)
print(1 is not 2)
'''
from testmodule import *
print getAge(111)
someone = People()
print someone.getName("wlt")