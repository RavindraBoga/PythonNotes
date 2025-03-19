import re
pattern=re.compile(r'([A-Za-z\s]+)\s+(\d{10})')

map={}
with open("Name&PhoneNumber.txt","r") as file:
    for line in file:
        match=pattern.search(line)
        if match:
            name,phn=match.groups()
            map[name.strip()]=phn
file.close()

with open("new.txt","w") as f:
    f.write(str(map))

f.close()