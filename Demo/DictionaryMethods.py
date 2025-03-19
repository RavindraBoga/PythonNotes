#clear--clear values in dict
dict={"n":"name",
      "p":"phon",
      "a":"add",
      "e":"email"
      }
print(dict)#{'n': 'name', 'p': 'phon', 'a': 'add', 'e': 'email'}
print(dict.clear())#None

#copy--copy values from one dict to another dict
dic1={1:"n",2:"p",3:"a",4:"e"}
dict2={2:"hi",1:"good",3:"hello"}
dic1=dict2.copy()
print(dic1)#{2:"hi",1:"good",3:"hello"}

#fromKeys---creates new dict with given keys and default values
#--- if default value is not provided None will be assigned to all keys

keys=[1,2,3,4]
defaultValue="hi"
new=dict.fromkeys(keys,defaultValue)
print(new)#{1: 'hi', 2: 'hi', 3: 'hi', 4: 'hi'}
#without default values
keys=[2,3,4,5,6]
n=dict.fromkeys(keys)
print(n)#{2: None, 3: None, 4: None, 5: None, 6: None}

#get---return value assosiated with key

d={1:"one",2:"two",3:"three",4:"four"}
print(d.get(2))#two
print(d.get(5))#None

#items()--returns an object with pairs sorted into tuple
dict={"name":"BVR","add":"KDP","Phn":8897841976}
for key,value in dict.items():
    print(f"{key}:{value}")
#o/p:name:BVR
    # add:KDP
    # Phn:8897841976

dict={"name":"BVR","add":"KDP","Phn":8897841976}
print(dict.items())#dict_items([('name', 'BVR'), ('add', 'KDP'), ('Phn', 8897841976)])

#keys---keys in an dict
dict={"name":"BVR","add":"KDP","Phn":8897841976}
print(dict.keys())#dict_keys(['name', 'add', 'Phn'])

#values---only values in adict
dict={"name":"BVR","add":"KDP","Phn":8897841976}
print(dict.values())#dict_values(['BVR', 'KDP', 8897841976])

#update--add all elements from one dict into another
dict={"name":"BVR","add":"KDP","Phn":8897841976}
dict2={1:"0ne",2:"two",3:"three",4:"four"}
dict.update(dict2)
print(dict)#{'name': 'BVR', 'add': 'KDP', 'Phn': 8897841976, 1: '0ne', 2: 'two', 3: 'three', 4: 'four'}

#pop--remove last element
dict.pop(4)
print(dict)#{'name': 'BVR', 'add': 'KDP', 'Phn': 8897841976, 1: '0ne', 2: 'two', 3: 'three'}

#popitem()--Removes and returns the last key-value pair as a tuple. Raises a KeyError if the dictionary is empty.
dict.popitem()
print(dict)#{'name': 'BVR', 'add': 'KDP', 'Phn': 8897841976, 1: '0ne', 2: 'two'}

#setdefault()--Returns the value of a specified key. If the key does not exist, it inserts the key with a specified default value.
values=dict.setdefault(10,"ten")
print(dict)#{'name': 'BVR', 'add': 'KDP', 'Phn': 8897841976, 1: '0ne', 2: 'two', 10: 'ten'}

