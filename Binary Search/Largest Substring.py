n=int(input())
s=input()
sumi,maxi=0,0
d={i:0 for i in range(n)}
for i in range(n):
  if s[i]=='0':
    sumi+=1
  else:
    sumi-=1
  if sumi>0:
    maxi=i+1
  else:
    if (sumi-1) in d:
      curlen=i-d[sumi-1]
      maxi=max(maxi,curlen)
  if sumi not in d:
    d[sumi]=i
print(maxi)
