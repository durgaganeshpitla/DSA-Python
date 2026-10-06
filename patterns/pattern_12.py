n = int(input())
for i in range(n-1):
   
    for j in range(i + 1):
       print(j + 1,end = "")
    for k in range(2*(n-1)-(2 * i+2)):
        print(" ",end="")
    for l in range(i,-1,-1):
        print(l+1 , end="")
      
    print()   