def feb(n):
    
    if (n==0):
        return 0
    elif(n==1):
        return 1
    else:
        k=feb(n-1)
        j=feb(n-2)
    return k+j
print(feb(7))

#recursive calls
def fib(n):
    if(n<=1):
        return 
        fib(n-2)
print(fib(7))