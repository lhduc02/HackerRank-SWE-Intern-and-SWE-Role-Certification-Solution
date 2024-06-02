n = int(input())

row, column = [], []
for i in range(n):
    a, b = [int(i) for i in input().split()]
    row.append(a)
    column.append(b)

print(min(row)*max(column))
