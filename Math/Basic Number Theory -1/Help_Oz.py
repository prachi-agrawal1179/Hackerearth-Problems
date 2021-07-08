import math

def gcd(a,b):
  if b==0:
    return a
  else:
    return gcd(b,a%b)

def divisors(n):
    divs = [1]
    for i in range(2,int(math.sqrt(n))+1):
        if n%i == 0:
            divs.extend([i,n//i])
    divs.extend([n])
    return list(set(divs))


m=int(input())
a=[]
for i in range(m):
  x=int(input())
  a.append(x)
a.sort()
z=[t - s for s, t in zip(a, a[1:])]
g=z[0]
for i in range(1,len(z)):
  g=gcd(g,z[i])

w=(divisors(g))
if 1 in w:
  w.remove(1)
if 0 in w:
  w.remove(0)
w=sorted(w)
print(*w,sep=' ')
