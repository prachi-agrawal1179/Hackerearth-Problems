import math

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=0
    x=a[0]
    for j in range(1,n):
        ans=math.gcd(x,a[j])
        x=ans
    if ans==1:
        print('FINITE')
    else:
        print('INFINITE')
