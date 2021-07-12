import math
t=int(input())
for j in range(t):
    a,b,n=map(int,input().split())
    if n%3==1:
        print(a)
    elif n%3==2:
        print(b)
    else:
        xor=a^b
        ans=int(math.log2(max(a,b))+1)
        final=(1<<ans)-1
        xnor=final^xor
        print(max(xor,xnor))
    
    
