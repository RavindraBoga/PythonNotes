import re

def re_C(ip):
    pattern=r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'

    if not re.match(pattern,ip):
        return False

    oct =ip.split(".")
    for octent in oct:
        if int(octent)<0 or int(octent)>255:
            return False
    return True

print(re_C("999.999.999.999"))
