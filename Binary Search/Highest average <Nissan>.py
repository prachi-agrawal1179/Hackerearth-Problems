import bisect
n=int(input())
a=list(map(int,input().split()))
a.sort()
sumi=[0]*n
x=[0]*n
sumi[0]=a[0]
x[0]=a[0]
for i in range(1,n):
  sumi[i]=a[i]+sumi[i-1]
  x[i]=sumi[i]/(i+1)  
    
q=int(input())
for i in range(q):
  k=int(input())
  maxi=bisect.bisect_left(x, k, lo=0, hi=len(x))
  # for j in range(n):
  #   if x[j]<k:
  #     maxi=j+1
  print(maxi)
