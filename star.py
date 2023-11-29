n=int(input())

lines = [ ['.' for i in range(n)] for i in range(n) ]
for i in range(n):
  # левая диагональ
  lines[i][i] = '*'
  # центральный столбец
  lines[i][n//2]='*'
  # правая диагональ
  lines[i][n - i - 1] = '*'
  # центральный ряд
  lines[n//2][i]='*'

for i in range(n):
  print(*lines[i])