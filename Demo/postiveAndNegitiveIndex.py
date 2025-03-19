list=eval(input("enter list"))
i=0
print("at even index")
while i<len(list):
    print(list[i],end=",")
    i=i+2
print()
print("at odd index")
i=1
while i<len(list):
    print(list[i],end=",")
    i=i+2