import re
def regExp(ip):
    pattern=r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'
    if not re.match(pattern,ip):
        return False
    octant=ip.split(".")
    for octants in octant:
        if int(octants)<0 or int(octants)>255:
            return False
    return True

print(regExp("333.333.333.333"))
