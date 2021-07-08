def modularExponentiation(x,n, M):
  if(n==0):
    return 1
  elif (n%2 == 0):
    return modularExponentiation((x*x)%M,n/2,M)
  else:                            
    return (x*modularExponentiation((x*x)%M,(n-1)/2,M))%M



q=10**9+7
a,b=map(int,input().split())
print(modularExponentiation(a,b,q))
