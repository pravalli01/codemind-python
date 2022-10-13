def is_ugly(num):
    if num==0:
        print('Not Ugly Number')
    for i in [2,3,5]:
        while num%i==0:
            num /=i
    return num==1
n=int(input())
c=is_ugly(n)
if (c==True):
    print('Ugly Number')
else:
    print('Not Ugly Number')