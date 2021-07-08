t=int(input())
for i in range(t):
    n=int(input())
    if n==1:
        print(1)
    else:
        ans=([n//2] + [n*(n-1)//2 - 1])
        print(sum(ans))
