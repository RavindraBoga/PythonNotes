# def w(ip):
#     oct=ip.split(".")
#     if len(oct)!=4:
#         return False
#     for octant in oct:
#         if not octant.isdigit():
#             return False
#         if int(octant)<0 or int(octant)>255:
#             return False
#     return True
#
# print(w("192.192.192.192"))

import re

def nr(ip):
 oct =ip.split(".")
 if len(oct)!=4:
   return False
 for o in oct:
   if not o.isdigit():
     return False
   num=int(o)
   if num<0 or num>255:
    return False
 return True

print(nr("192.255.192.192"))