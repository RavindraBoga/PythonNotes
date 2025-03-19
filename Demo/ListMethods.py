#sum--sum of all values
list=[1,2,3,4]
print(sum(list))#10

#lindex--index of values
print(list.index(3))#2

#len--length of list
print(len(list))#4

#append--add value
list.append(100)
print(list)#[1,2,3,4,100]

#insert--insert at particular index
list.insert(2,20)
print(list)#[1,2,20,3,4,100]

#copy--copy new list into existing list
list2=[10,20,30,40]
list=list2.copy()
print(list)#[10,20,30,40]

#extend--add new list into existing list
list=[10,20,30,40]
list.extend([1,2,3,4,5])
print(list)#[10,20,30,40,1,2,3,4,5]

#count--no of occurance of value in a list
l=[5,8,1,4,10,30,1]
print(l.count(1))#2

#remove--emove element in a list
l.remove(1)
print(l)#[5,8,4,10,30,1]

#pop()--remove ending element of list
l.pop()
print(l)#[5,8,4,10,30]

#sort--sort elements in the list
new=[100,2,200,4,1,0]
new.sort()
print(new)#[0,1,2,4,100,200]

#reverse--reverse the values in a list
new.reverse()
print(new)#[200,100,4,2,1,0]

#clear()--clear values in the list
new.clear()
print(new)#[]


