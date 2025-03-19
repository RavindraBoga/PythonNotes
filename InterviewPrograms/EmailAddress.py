# import re
# def email(mail):
#     pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
#     if re.match(pattern,mail):
#         return True
#     return False
#
# print(email("ravindraboga178@gmail.in"))
import re
def email(mail):
	pattern=r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
	if re.match(pattern,mail):
		return True
	return False
print(email("raviboga178@gmail.com"))
