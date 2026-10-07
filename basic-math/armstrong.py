n = 153
arm = n
sum = 0
while n > 0 :
    digit = n % 10
    sum = sum + (digit * digit * digit) 
    n = n // 10
if sum == arm: 
    print (True) 
else:
    print (False)   