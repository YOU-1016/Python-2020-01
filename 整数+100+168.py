import math  #调用函数math
for x in range(999999): #使用循环变量寻找未知数X
    num1 = int(math.sqrt(x + 100))#第一个完全平方数的平方根
    num2 = int(math.sqrt(x + 100 +168)) #第二个完全平方数的平方根
    if (num1*num1 == x+100) and (num2*num2 == x+100+168) : #判断条件：平方根平方等于未知数加100，平方根平方对于未知数加268，同时满足条件输出条件。
        print(x)#输出未知数x
