import random
number = random.randint(1,10)
A = []
for i in range(0,4):
    temp = []
    for j in range(0,4):
        temp.append(number)
        number = random.randint(1,10)
    A.append(temp)
print(A)

for r in range(len(A)):
    c = A[r].index(max(A[r]))
    k = 0
    while k < len(A):
        if A[r][c] <= A[k][c]:
            k += 1
            if k == len(A):
                print('鞍点在第{}行，第{}列，值为：{}'.format(r + 1, c + 1, A[r][c]))
            else:
               print("未找到鞍点")
        else:
           break
              
