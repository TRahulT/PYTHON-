num= int(input("no. of element"))
list1=[int(input("enter the element "))for value in range(num)]
for i in range(len(list1)-1):
    for j in range(i+1,len(list1)):
        if list1[j]>list1[i]:
            list1[i],list1[j]=list1[j],list1[i]
print(list1)