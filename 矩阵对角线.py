import random
number = random.randint(1,10)
A = []
for i in range(0, 5):
    temp = []
    for j in range(0, 5):
        temp.append(number)
        number = random.randint(1,10)
    A.append(temp)
print(A)

sum1 = 0
sum2 = 0
for i in range(5):
   sum1 += A[i][i]
   sum2 += A[4-i][i]
print('从左上到右下数组之和：',sum1)

print('从左下到右上数组之和：',sum2)
