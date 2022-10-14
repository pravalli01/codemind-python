import re
string = input()
total_digits=len(re.findall('[0-9]',string))
if(total_digits > 0):
    print("Contains {} digit".format(total_digits))
else:
    print("Doesn't contain digit")