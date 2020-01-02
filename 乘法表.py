#作者：游成伟
#创始时间：2019-10-29

for i in range(1,10):#定义i的取值范围
    for j in range(1,i+1):#在已定义i数值的基础上定义j的范围
        print(str(j) + str("*") + str(i)+"=" + str(i*j),end="\t")#在定义两个数值之后进行相乘并输出完整的计算过程完成乘法表
    prin()
