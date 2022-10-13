num=int(input())
count=0
for i in range(num):
    if i*(i+1)==num:
        count=1
        break
if count==1:
    print("YES")
else:
    print("NO")