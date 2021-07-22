t=int(input())
for i in range(t):
  x=int(input())
  if x%21==0 or '21' in str(x):
    print('The streak is broken!')
  else:
    print('The streak lives still in our heart!')
