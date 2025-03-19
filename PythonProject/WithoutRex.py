import re

def without_Re(ip):
    octant=ip.split(".")

    if len(octant)!=4:
        return False
    for oct in octant:
        if not oct.isdigit():
            return False
        num=int(oct)
        if num<0 or num>255:
            return False
    return True

print(without_Re("192.192.192.192"))