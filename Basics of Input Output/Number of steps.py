n=int(input())

a=list(map(int,input().split()))

b=list(map(int,input().split()))

k=min(a)

c=0

flag=True

for i in range(n):
  while(a[i]>k and b[i]!=0):
    a[i]=a[i]-b[i]
    c=c+1
  if(a[i]<0):
    flag=False
    break
  else:
    k=min(a)

for i in a:
  if(i!=min(a)):
    flag=False
    break

if(flag==False):
  print("-1")

else:
  print(c)
