def solve (A):
  even,odd=0,0
  x=len(A)//2
  for i in range(len(A)):
    if i%2==0 and i<x:
      even+=int(str(A[i])[0])
    elif i%2==0 and i>=x:
      even+=int(str(A[i])[-1])
    elif i%2!=0 and i>=x:
      odd+=int(str(A[i])[-1])
    elif i%2!=0 and i<x:
      odd+=int(str(A[i])[0])
  if (even-odd)%11==0:
    return 'OUI'
  else:
    return 'NON'
    # Write your code here

N = int(input())
A = list(map(int, input().split()))

out_ = solve(A)
print (out_)
