str=input("enter string")
i=0
for x in str:
    print(" char at +ve index is {} and -ve index {} is{}".format(i,i-len(str),x))
    i=i+1
