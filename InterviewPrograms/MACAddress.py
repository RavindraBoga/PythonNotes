import re
def MAC(mac):
    pattern=r'^([0-9A-Fa-f]{2}([:-])){5}([0-9A-Fa-f]{2})$'
    #pattern_cisco = r'^([0-9A-Fa-f]{4}\.){2}[0-9A-Fa-f]{4}$'
    if re.match(pattern,mac):
        return True
    return False

print(MAC("00-1A-2B-3C-4D-5E"))