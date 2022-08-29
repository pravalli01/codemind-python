t=int(input())
while t:
    t -= 1
    count =0
    x,y=input().split()
    i=x
    while int(i) <= int(y):
        if i[-1]=='2'or i[-1]=='3'or i[-1]=='9':
            count +=1
        i=str(int(i)+1)
    print(count)    