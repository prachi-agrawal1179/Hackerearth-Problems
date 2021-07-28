def binary_search(a,x,n):
  l,r=0,n-1
  while l<=r:
    m=(l+r)//2
    if x==a[m]:
      return 1
    elif x<a[m]:
      r=m-1
    else:
      l=m+1
  return -1

n,q=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
for i in range(q):
  x=int(input())
  ans=binary_search(a,x,n)
  if ans==-1:
    print('NO')
  else:
    print('YES')
        
