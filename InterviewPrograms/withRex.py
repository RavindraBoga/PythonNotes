import re
def rex(ip):
    pattern=r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    pattern = r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    if not re.match(pattern,ip):
        return False
    oct=ip.split(".")
    for o in oct:
        if int(o)<0 or int(o)>255:
            return False
    return True

print(rex("192.168.1.1"))