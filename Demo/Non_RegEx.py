import re
def non_regExp(ip):
    octants= ip.split(".")
    if len(octants)!=4:
        return False
    for octan in octants:
        if not octan.isdigit():
            return False
        num=int(octan)
        if num<0 or num>255:
                return False
    return True

print(non_regExp("256.162.1.1"))
