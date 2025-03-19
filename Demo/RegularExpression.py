import re
def non_regEx(ip):
    pattern=r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    if not re.match(pattern,ip):
        return False
    octent =ip.split(".")
    for octents in octent:
        if int(octents)<0 or int(octents)>255:
            return False
    return True
print(non_regEx("192.168.1.1"))