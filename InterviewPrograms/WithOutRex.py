def without_rex(ip):
    oct=ip.split(".")

    if len(oct)!=4:
        return False
    for o in oct:
        if not o.isdigit():
            return False
        if int(o)<0 or int(o)>255:
            return False
    return True

print(without_rex("192.168.1.1"))