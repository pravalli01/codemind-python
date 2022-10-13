import math
n=int(input())
a=math.sqrt(n)
if(n%a==0 and n>0):
    print('True')
else:
    print('False')