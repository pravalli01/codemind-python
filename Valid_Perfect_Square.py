import math
n=int(input())
for i in range(n):
    a=int(input())
    b=math.sqrt(a)
    if(a%b==0 and n>0):
        print('True')
    else:
        print('False')