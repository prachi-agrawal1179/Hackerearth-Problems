t=int(input())
for i in range(t):
    n=int(input())
    print((n*(2*n-1)%(10**9+7)))
    # a,b,c=1,6,5
    # q=10**9+7
    # if n==1:
    #     print(1)
    # elif n==2:
    #     print(6)
    # else:
    #     ans=6
    #     y=5
    #     for i in range(2,n):
    #         y=y+4
    #         ans=ans+y
    #     print(ans)
