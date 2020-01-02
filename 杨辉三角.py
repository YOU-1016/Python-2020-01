t = int(input("输入杨辉三角的行数:"))
def triangles(t):#定义函数用于排列杨辉三角
   print([1])    #第一行
   print([1,1])  #第二行
   p2  = [1,1]
   for i in range(2,t):#用循环来生成目标行数
      r = []
      for i in range(0,len(p2)-1):#利用循环来生成每一行的数值
         r.append(p2[i]+p2[i+1])#利用杨辉三角除两边是1外其余的数是上一层的两个数之和的特征
      p2 = [1] + r + [1]#在两端加上“1”
      print(p2)
triangles(t)#输出函数

        
   
