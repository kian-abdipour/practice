import re


#a = "4444"
#x = re.search("^\\d{4}$", a)
#if x:
#    print("Ok")
#
#else:
#    print("No")


s = "mb23"
match = re.search('^[a-z][0-9]$', s)
if match:
    print("YES")

else:
    print("NO")


condition = re.search('^[A-Za-z]{2}[0-9]{6}\s[0-9]{8}$', "MG123456 12345678")
if condition:
    print("YES")

else:
    print("NO")

