MOD=1000000009

def power( x,  y):
    res=1
    x%=MOD
    while(y>0):
        if(y&1):
            res=(res*x)%MOD
        y>>=1
        x=(x*x)%MOD
    return res;

t=int(input())
for i in range(t):
    n=int(input())
    print((((power(10,n)-power(8,n))+MOD)*500000005)%MOD)
