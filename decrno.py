def dec(n):
    if n==0:
        return
    else: 
        print(n)
        dec(n-1)
print(dec(8))