n = int(input())

for m in range(0,n):

  spisock = ["_" for i in range(n)]
  for i in range(m,n):
    spisock[i]= i - m

  for i in range(m):
    spisock[i]= m - i

  print(*spisock)
