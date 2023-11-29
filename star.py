n = int(input())

lines = [['.' for i in range(n)] for i in range(n)]
for i in range(n):
    lines[i][i] = '*'
    # как узнать индекс центральной линии используя число n?
    lines[n // 2][i] = '*'
    lines[i][n - i - 1] = '*'

    print(*lines[i])