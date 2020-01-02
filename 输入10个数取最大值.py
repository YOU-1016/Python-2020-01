list = []
for i in range(1,11):
   x = int(input("请输入第%s个数值："%i))
   list.append(x)
a = sorted(list)
print("最大值为：",a[9])
