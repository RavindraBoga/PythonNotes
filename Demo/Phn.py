import re
def phn(ph):
    pattern=r'^\d{10}$'
    if re.match(pattern,ph):
        return True
    return False

print(phn("123456789+"))