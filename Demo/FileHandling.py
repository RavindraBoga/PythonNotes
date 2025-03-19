import re
pattern=re.compile(r'([A-Za-z\s]+)\s+(\d{10})')
dict={}
with open("N&P.txt","r") as file:
    for line in file:
        match=pattern.search(line)
        if match:
            name,phn=match.groups()
            dict[name.strip()]=phn
with open("DN&P.txt","w") as f:
    f.write(str(dict))
