#having pivot present at first 
def pivot_place(li,first,last):
    pivot=li[first]
    left=first+1
    right=last
    while True:
        while left<=right and li[left]<=pivot:
            left=left+1
        while left<=right and li[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            li[left],li[right]=li[right],li[left]
    li[first],li[right]=li[right],li[first]
    return right
def quicksort(li,first,last):
    if first<last:
        p=pivot_place(li,first,last)
        quicksort(li,first,p-1)
        quicksort(li,p+1,last)

li=[3,43,12,44,32,5]
n=len(li)
quicksort(li,0,n-1)
print(li)