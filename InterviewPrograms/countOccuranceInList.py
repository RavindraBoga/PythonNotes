# # list=[1,3,2,2,4,2,1]
# # value=1
# # count=0
# # for i in list:
# #     if i==value:
# #         count=count+1
# # print(count)
#
# list=[1,2,1,2,2]
# print(list.count(1))

#
# s="ravindra"
# l=list(s)
# count=0
# value=input("enter char")
# for i in l:
#     if i==value:
#         count+=1
# print(count)
s="ravindra"
l=list(s)
count=0
value=input("enter char")
for i in l:
	if i==value:
		count+=1
print(f"{value} count is {count}")