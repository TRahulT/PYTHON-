#having pivot present at last
def pivot_place(li,first,last):
    pivot=li[last]
    left=first
    right=last-1
    while True:
        while left<=right and li[left]<=pivot:
            left=left+1
        while left<=right and li[right]>=pivot:
            right=right-1
        if right<left:
            break
        else:
            li[left],li[right]=li[right],li[left]
    li[last],li[left]=li[left],li[last]
    return left
def quicksort(li,first,last):
    if first<last:
        p=pivot_place(li,first,last)
        quicksort(li,first,p-1)
        quicksort(li,p+1,last)

li=[3,43,12,44,32,5]
n=len(li)
quicksort(li,0,n-1)
print(li)