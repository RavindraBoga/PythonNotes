# list=[20,1,30,5,10]
# list[2],list[0]=list[0],list[2]
# print(list)

#approach--2

list=[10,2,3,4,5]
l1=list.pop(1)
l2=list.pop(2)
list.insert(2,l1)
list.insert(1,l2)
print(list)