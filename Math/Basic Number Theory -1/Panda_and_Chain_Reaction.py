import math
def fact(n,x,q):
    
    if n<=10**5:
        x=((q[n])*x)%(10**6+3)
    else:
        x=0
    
    return x

q=(10**5+1)*[0]
q[0]=1
for i in range(1,10**5+1):
    q[i]=(q[i-1]*i)%(10**6+3)
n=int(input())
for i in range(n):
    n,x=map(int,input().split())
    print(fact(n,x,q))
