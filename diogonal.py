 #Дано число n и m. Нужно создать список размера n, где под индексом m находится 0, после нуля по возрастанию идут целые числа, а до нуля идут числа по убыванию

n = 6 # int(input())
m = 3 # int(input())

# spisock=[3, 2, 1, 0, 1, 2]
spisock = ["_" for i in range(n)]
for i in range(m,n):
    spisock[i]= i - m

for i in range(m):
  spisock[i]= m - i
print(spisock)
