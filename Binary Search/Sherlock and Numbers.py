n=int(input())
for i in range(n):
  n,k,p=map(int,input().split())
    
  x=list(map(int,input().split()))
  for j in range(k):
    if x[j]<=p:
      p+=1
  if p>n:
    print(-1)
  else:
    print(p)
        
