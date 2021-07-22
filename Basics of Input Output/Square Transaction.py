import bisect as b
N=int(input())
a=list(map(int,input().split()))
sumi = [0]
for v in a:
  sumi+=[sumi[-1]+v]

q=int(input())
for i in range(q):
  x=int(input())
  ans=b.bisect(sumi,x)

  if ans==N+1 and sumi[-1]!=x:
    print(-1)

  else:
    if(sumi[ans-1]==x):
      print(ans-1)

    else:
      print(ans)
