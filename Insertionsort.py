def insertionsort(mylist):
    for index in range(1,len(mylist)):
        current_element=mylist[index]
        pos=index
        while current_element>mylist[pos-1] and pos>0:
            mylist[pos]=mylist[pos-1]
            pos=pos-1
        mylist[pos]=current_element
list1=[4,54,2,44,3,6]
insertionsort(list1)
print(list1)