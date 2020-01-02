for num in range(100, 1000):
   gewei = num % 10
   shiwei = num // 10 % 10
   baiwei = num//100
   if gewei**3 + shiwei**3 + baiwei**3 == num:
      print(num)
