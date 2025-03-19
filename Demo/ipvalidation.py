# '''
# import re
#
# def validate_ip_with_regex(ip_address):
#     pattern = re.compile(
#         r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'  # First octet
#         r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'  # Second octet
#         r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.'  # Third octet
#         r'(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'  # Fourth octet
#     )
#     return pattern.match(ip_address) is not None
#
# # Example usage
# print(validate_ip_with_regex("192.168.1.1"))  # True
# print(validate_ip_with_regex("256.256.256.256"))  # False
#
# print(validate_ip_with_regex("192.168.01.1"))
# '''
# import re
#
# def is_valid_ipv4(ip):
#     # IPv4 pattern: 4 sets of 1-3 digit numbers (0-255) separated by '.'
#     pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'
#
#     return bool(re.match(pattern, ip))
#
# # Test Cases
# print(is_valid_ipv4("192.168.1.1"))   # True
# print(is_valid_ipv4("255.255.255.255")) # True
# print(is_valid_ipv4("256.100.50.25"))   # False (256 is invalid)
# print(is_valid_ipv4("192.168.1"))       # False (not 4 octets)
# print(is_valid_ipv4("192.168.01.1"))    # False (leading zero)
import re
def adreg(ip):
#   pattern:r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    pattern = r'^((25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$'

    if re.match(pattern,ip):
	    return True
    return False

print(adreg("192.192.192.257"))
