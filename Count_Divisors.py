x,y,z=map(int,input().split())
count=0
for i in range (x,y+1):
    if(i%z==0):
        count+=1
print(count)    