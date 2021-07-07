def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)


n=int(input())
l=list(map(int,input().split()))
q=10**9 + 7
g=l[0]
f=l[0]
for i in range(1,n):
  g=gcd(g,l[i])
  f=f*l[i]
print((f**g)%q)





