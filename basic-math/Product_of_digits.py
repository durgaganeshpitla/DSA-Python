n = 1234
pro = 1
while n > 0 :
    digit = n % 10
    pro = pro * digit
    n = n // 10
print(pro)    