import re

File1="N&P.txt"
File2="DN&P.txt"
pattern=re.compile(r'([A-Za-z\s]+)\s+(\d{10})')
dict={}

with open(File1,"r") as File:
    for line in File:
        match=pattern.search(line)
        if match:
            name,phn=match.groups()
            dict[name.strip()]=phn


with open(File2,"w") as file:
    file.write(str(dict))




