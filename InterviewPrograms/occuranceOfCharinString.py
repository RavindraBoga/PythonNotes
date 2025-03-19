# from collections import Counter
# s="ravindra"
# count=Counter(s)
#
# print(count["r"])
s="ravindra"
l=list(s)
value="r"
count=0
for i in l:
    if i==value:
     count=count+1
print(count)