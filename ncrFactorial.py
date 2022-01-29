def ncr(n,r):
    def fac(k):
        if k==1:
            return 1
        else:
            l=fac(k-1)
            return k*l
    j=int(fac(n)/(fac(n-r)*fac(r)))

    return j
print(ncr(5,2))
    