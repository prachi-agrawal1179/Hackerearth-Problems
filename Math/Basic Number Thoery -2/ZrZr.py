def zeros(n):
    x=5
    ans=0
    while n/x>=1:
        ans+=n//x
        x*=5
    return ans

t=int(input())
for i in range(t):
    n=int(input())
    print(zeros(n))
