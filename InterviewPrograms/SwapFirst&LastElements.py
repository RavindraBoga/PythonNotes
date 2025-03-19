#approach--1
# list=[0,1,2,3,4,5]
# n=len(list)
# temp=list[0]
# list[0]=list[n-1]
# list[n-1]=temp
# print(list)

#Approach-2
# list=[1,10,2,20,30,3]
# list[0],list[-1]=list[-1],list[0]
# print(list)

#approach-3
list=[1,10,2,20,30,3]
n=list.pop(0)
n2=list.pop(-1)
list.insert(0,n2)
list.append(n)
print(list)