import math
Number=int(input())
sum=0
sqr=math.pow(Number,2)
while sqr>0:
    rem=sqr%10
    sum=sum+rem
    sqr=sqr//10
if sum==Number:
    print("Neon Number")
else:
    print("Not Neon Number")