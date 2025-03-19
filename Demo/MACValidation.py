import re
def macc(mac):
    pattern=r'^([0-9A-Fa-f]{2}([-:])){5}([0-9A-Fa-f]{2})$'
    if re.match(pattern,mac):
        return True
    return False
print(macc("00-1A-2B-3C-4D-E5"))
print(macc("00:1a:2b:3c:4d:dd"))