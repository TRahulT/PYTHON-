def inc(n):
    if n==0:
        return
    else:
        inc(n-1)

        print(n)
print(inc(6))