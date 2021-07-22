def minCost(A,B,N):

  return round((N*B)/(A+B))

 

def findCost(A,B,X,Y):

  return A*(X**2)+B*(Y**2)

 

t = int(input())  

for i in range(t):

  N,A,B = map(int, input().split())

  L1 = minCost(A, B, N)

  print(findCost(A,B,L1,N-L1))
