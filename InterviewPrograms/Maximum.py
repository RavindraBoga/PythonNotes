# list=[3,10,500,100]
# # print(max(list))
# # print(min(list))
#
# max=list[0]
# n=len(list)
# for i in range (1,n):
#     if list[i]>max:
#         max=list[i]
#
# print("max value is",max)
list=[1,2,3,4,5,0,-100]
min=list[0]
for i in range(1,len(list)):
	if list[i]<min:
		min=list[i]
print(min)