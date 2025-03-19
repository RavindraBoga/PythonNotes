s=input("ENter String")
list=s.split()
empty=[]
i=len(list)-1
while i>=0:
    empty.append(list[i])
    i=i-1
 #   print(empty)
output=" ".join(empty)
print(output)