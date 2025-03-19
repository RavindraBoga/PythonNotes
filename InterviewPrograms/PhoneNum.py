import re
def phn(ph):
    pattern=r'^(\+91[\-\s]?)?[0]?\d{10}$'
    if re.match(pattern,ph):
        return True
    return False
#print(phn("8897841976"))
print(phn("+91 1234567890"))
print(phn('09876543211'))
print(phn('+911234567890'))