s=input("enter some string")
l=s.split()
e=[]
#i=len(s)-1
for x in l:
    e.append(x[::-1])
print(e)
output=" ".join(e)
print(output)