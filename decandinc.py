def decinc(n):
    if (n==0 ):
        return
    else:
        print(n)
        decinc(n-1)
        return(n)
print(decinc(5))