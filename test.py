import re


a = "4444"
x = re.search("^\\d{4}$", a)
if x:
    print("Ok")

else:
    print("No")

