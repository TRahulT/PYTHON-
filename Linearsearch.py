#no duplicate in list'
def lisearch(arr,key):
    for i  in range(len(arr)):
        if key==arr[i]:
            print('element is found at index',i)
            break
    else:
        print('element is not found ')

arr=[4,54,22,43,55,43,65,64]
print(arr)
key=int(input('enter the value of key element'))
lisearch(arr,key)
#linear search for duplicaton

def linearsearch(arr,key):
    arr2=[]
    flag=False
    for i in range(len(arr)):
        if key==arr[i]:
            flag=True
            arr2.append(i)
    if flag==True:
        print('key is found')
        for i in arr2:
            print(i)
    else:
        print('key is not found')
arr1=[34,43,55,6,2,34,65,76,4]
print(arr1)
key1=int(input('enter the key element:'))
linearsearch(arr1,key1)

