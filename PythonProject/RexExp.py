import re

def rex(ip):
    pattern=r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'

    if re.match(pattern,ip):
        return True
    return False

print(rex("0.0.0.0"))
