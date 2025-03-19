list=[10,3,5,1,0,-100]
min=list[0]
n=len(list)
for i in range(1,n):
    if list[i]<min:
        min=list[i]
print("min value is",min)