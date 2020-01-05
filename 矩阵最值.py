from random import randint
b=0
s=''
l=[]
mini=[]
for i in range(1,26):
    rnd=randint(1,9999)
    l.append(rnd)
    s+=" "+str(rnd)
    if i%5==0:
        print(s)
        s=''
for i in range(1,6):
    min1=(i-1)*5
    for j in range((i-1)*5,5*i):
        if l[min1]>l[j]:
            min1=j
    else:
        min2=min1
        for k in range(min1-i*5+5,min1+(5-i)*5,5):
            if l[min2]>l[k]:
                min2=k
        if l[min1]==l[min2]:
            mini.append(l[min1])
            print('第%d个5*5的矩阵中所在行和所在列均是最小的数为%d,其坐标为(%d,%d)'%(b+1,mini[b],min1//5+1,min1%5))
            b+=1
