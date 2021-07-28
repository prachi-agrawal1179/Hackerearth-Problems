n=int(input())
ans={}
for i in range(n):
  s=input().split()
  s.sort()
  s = "".join(s)
  if s not in ans:
    ans[s] = 1
  else:
    ans[s] += 1

count = 0
for key in ans:
  if ans[key] == 1:
    count+=1
print(count)
