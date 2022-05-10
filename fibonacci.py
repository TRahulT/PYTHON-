def feb(n):
    
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        k=feb(n-1)
        j=feb(n-2)
        return k+j
num=int(input())
for i in range(num):
    print(feb(i))
