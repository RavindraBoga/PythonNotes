import re

def non_rex(ip):
    octent=ip.split(".")

    if len(octent)!=4:
        return False

    for octant in octent:
        if not octant.isdigit():
            return False
        num=int(octant)
        if num<0 or num>255:
            return False
    return True

print(non_rex("192.192.192.259"))