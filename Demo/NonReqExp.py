def non_Req_Expression(ip):
    octants=ip.split(".")
    if len(octants)!=4:
        return False
    for octant in octants:
        if not octant.isdigit():
            return False
        num=int(octant)
        if num<0 or num>255:
            return False
    return True

print(non_Req_Expression("266.168.1.1"))