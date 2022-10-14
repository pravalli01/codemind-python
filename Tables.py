a,b=map(int,input().split())
i=1
while(i<=b):
    if(i%2!=0):
        print(a,"x",i,"=",i*a)
    i+=1