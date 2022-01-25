def binarysearch(list1,key):
    low=0
    high=len(list1)-1
    found=False
    while low<=high and not found:
        mid=(low+high)//2
        if key==list1[mid]:
            found =True
        elif(key>list1[mid]):
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print('key is found')
    else:
        print('key is not found')
num=(int(input('enter the numbers we want to insert in the list1:')))
list1=[int(input('enter values:'))for values in range(num)]
list1.sort()
print(list1)
key=int(input('enter the key value:'))
binarysearch(list1,key)
