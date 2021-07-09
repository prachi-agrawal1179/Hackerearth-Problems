import math
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    ans=a[0]
    for j in range(1,n):
        ans=(ans*a[j])//(math.gcd(ans,a[j]))
    print(ans)
