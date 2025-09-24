n = int(input())

matrix = []
for _ in range(n):
    matrix.append([int(x) for x in input().split()])
primary_diagonal = [matrix[i][i] for i in range(n)]
secondary_diagonal = [matrix[i][-i - 1] for i in range(n)]

print(abs((sum(primary_diagonal) - sum(secondary_diagonal))))
