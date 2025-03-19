#len--length of tuple
t=(2,5,1,4,5,9,2)
print(len(t))#7

#min---smallest value in tuple
print(min(t))#1

#max--largest value in the tuple
print(max(t))#9

#count--no of occurance for a values in tuple
print(t.count(2))#2

#index--first occurance of element in tuple
print(t.index(2))#0

#sorted ---sort the tuple into a new list
list=sorted(t)
print(list)#[1,2,2,4,5,5,9]

#convert list into tuple
tuple1=tuple(list)
print(tuple1)#(1,2,2,4,5,5,9)
