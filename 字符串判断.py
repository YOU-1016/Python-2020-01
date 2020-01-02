s = input("请输入字符串")
qt = 0     #定义各个元素的初始值
kg = 0
sz = 0
zm = 0
for i in s:             #历遍输入的字符串
   if i.isspace():      #利用函数找到空格
      kg += 1#空格个数加一
   elif i.isdigit():    #利用函数找到数字
      sz += 1#数字个数加一
   elif i.isalpha():    #利用函数找到字母
      zm += 1#字母个数加一
   else:                #剩下的为其他
      qt += 1
print("字母个数:",zm,"数字个数:",sz,"空格个数:",kg,"其他:",qt)#输出结果
