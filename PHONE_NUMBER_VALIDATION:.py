import re
n=input()
r=re.fullmatch('[6-9][0-9]{9}',n)
if r!=None:
    print("Valid")
else:
    print("Invalid")