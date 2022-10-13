n=int(input())
s=0
t=n
while(n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
    s=s+f
    n=n//10
if(s==t):
    print("The number {} is a strong number".format(t))
else:
    print("The number {} is not a strong number".format(t))