a=int(input())
b=int(input())
for m in range(a,b+1):
    num=m
    d=num
    rev=0
    while(num>0):
        r=num%10
        rev=(rev*10)+r
        num=num//10
    if(d==rev):
        print(d,end=' ')