import re
def non_Req(ip):
    pattern=r'^([0-9]{1,3}\.){3}[0-9]{1,3}$'

    if not re.match(pattern,ip):
        return False
    octents=ip.split(".")
    for octent in octents:
        if int(octent)<0 or int(octent)>255:
            return False
    return True
print(non_Req("192.192.192.192"))


