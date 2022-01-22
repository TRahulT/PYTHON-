
def mergesort(list1):
    if len(list1)>1:
        mid=len(list1)//2
        n1=list1[:mid]
        n2=list1[mid:]
        mergesort(n1)
        mergesort(n2)
        #intially i=0 we use as index l1 sublist ,j=0 for l2 
        i=0
        j=0
        k=0
        while i<len(n1) and j<len(n2):
            if n1[i]>n2[j]:
                list1[k]=n1[i]
                i=i+1
                k=k+1
            else:
                list1[k]=n2[j]
                j=j+1
                k=k+1
        while i<len(n1):
            list1[k]=n1[i]
            i=i+1
            k=k+1
        while j<len(n2):
            list1[k]=n2[j]
            j=j+1
            k=k+1
num=int(input("enter the number of element in list:"))
list1=[int(input('enter the value'))for i in range(num)]
mergesort(list1)
print(list1)


            

