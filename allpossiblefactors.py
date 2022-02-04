def fact(n):
    fac=[]
    for i in range(1,n+1):
        if n%i==0:
            fac=fac+[i]
    return fac
print(fact(442))
def fc(n):
    fac=[]
    for  i in range(1,n+1):
        if n%i==0:
            fac.append(i)
    return fac
print(fc(442))