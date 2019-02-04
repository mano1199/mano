name= int(input())
sum = 0
temp = name
while temp > 0:
   d= temp % 10
   sum += d ** 3
   temp //= 10
if name == sum:
   print('yes')
else:
   print('no')
