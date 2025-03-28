# keys=["a",'b','c','d']
# values=[1,2,3,4]
# myDict={k:v for (k,v) in zip(keys,values)}
# print(myDict)
#
# k=["Name","age","city"]
# v=["RAvi","28","Bang"]
# dict=dict(zip(k,v))
# print(dict)

keys = ['name', 'age', 'city']
values = ['Ravindra', 25, 'Bengaluru']

dictionary = {}
for i in range(len(keys)):
    dictionary[keys[i]] = values[i]

print(dictionary)
