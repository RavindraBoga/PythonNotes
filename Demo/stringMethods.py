s=input("enter string")
list=s.split()
empty=[]
for x in list:
    empty.append(x[::-1])
print(" ".join(empty))

