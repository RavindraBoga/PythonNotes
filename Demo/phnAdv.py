import re
def phn(ph):
    pattern=r'^(\+91[\-\s]?)?[0]?\d{10}$'
    if re.match(pattern,ph):
        return True
    return False

print(phn("9876543210"))
print(phn("+91-9876543210"))
print(phn("09876543210"))
print(phn("1234567890"))