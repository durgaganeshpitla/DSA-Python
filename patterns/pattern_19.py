n = int(input())
for i in range(n):
    print("*" * (n-i),end = "")
    print(" " * (2*i),end="")
    print("*" * (n-i))   
    
for j in range(1,n+1):
    print("*" * j,end = "")
    print(" " * (2 * (n -j)),end = "")
    print("*" * j)