s=input("enter string")
#print("char at even are :",s[::2])
#print("char at odd are :",s[1::2])

i=0
print("at even position")
while i<len(s):
    print(s[i],end=",")
    i=i+2

i=1
print()
print("at odd position")
while i<len(s):
    print(s[i],end=":")
    i=i+2