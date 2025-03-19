# #using looping
# num=10
# factorial=1
# if num>0:
#     for i in range(1,num+1):
#         factorial=factorial*i
#     print(factorial)

#using recursive function
# def fact(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*fact(n-1)
# num=5
# print(fact(num))

# ##using Ternari approach
# def fact(n):
#     return 1 if (n==0 or n==1) else n*fact(n-1)
# num=4
# print(fact(num))
#
# num=int(input("enter num"))
# fact=1
# if num>0:
#     for i in range(1,num+1):
#         fact=i*fact
#     print(fact)

import math
print(math.factorial(5))