a=int(input())
b=int(input())
c=0
d=0
for i in range(1,a+1):
    if(a%i==0):
        c+=i
for j in range(1,b+1):
    if(b%j==0):
        d+=j
        if(c==d):
             print("Amicable")
             break
else:
    print("Not Amicable")
        
        