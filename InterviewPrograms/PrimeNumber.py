# num=3
# count=0
# if num>1:
#     for i in range(1,num+1):
#         if num%i==0:
#             count+=1
#     if count==2:
#         print("prime")
#     else:
#         print("nor prime")
# else:
#     print("enter natural number")

num=10
count=0
if num>1:
	for i in range(1,num+1):
		if num%i==0:
			count=count+1
	if count==2:
		print("prime")
	else:
		print("not prime")
else:
	print("enter naturl num")
