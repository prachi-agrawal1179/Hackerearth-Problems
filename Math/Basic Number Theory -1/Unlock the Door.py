import math
q=10**9+7
t=int(input())
for i in range(t):
    n,k=map(int,input().split())
    ans=math.factorial(k)//math.factorial(k-n)
    print(ans%q)
