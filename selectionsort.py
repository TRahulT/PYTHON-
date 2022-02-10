
#use of min built in function for selection sort
list1=[32,3,94,85,4,3,2,0]
print(list1)
for i in range(len(list1)-1):
    min_val=min(list1[i:])
    min_index=list1.index(min_val,i)
    list1[i],list1[min_index]=list1[min_index],list1[i]
print(list1)
#to sort in decending order we just replace it by max function
m=int(input("how many numbers you want insert :"))
list2 =[int(input('enter the number')) for values in range(m)]
for i in range(len(list2)-1):
    m_val=i
    for j in range(i+1,len(list2)):
        if list2[j]<list2[m_val]:
            m_val=j
    list2[i],list2[m_val]=list2[m_val],list2[i]
print(list2)
            