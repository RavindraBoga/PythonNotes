import re
s=re.compile('[@_!#$%^&*()<>?/\|}{~:]')
string="!WELVK"
if s.search(string):
    print("found")
else:
    print("not found")