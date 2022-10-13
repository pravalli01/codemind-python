import math
Number=int(input())
s=0
sqr=math.pow(Number,2)
while sqr>0:
    rem=sqr%10
    s=s+rem
    sqr=sqr//10
if s==Number:
    print("Neon Number")
else:
    print("Not Neon Number")