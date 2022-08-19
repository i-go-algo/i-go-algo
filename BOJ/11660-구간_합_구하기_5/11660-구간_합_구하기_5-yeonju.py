import sys
input = sys.stdin.readline
n, m = map(int, input().split())

matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    for i in range(1, len(row)):
        row[i] += row[i - 1]
    matrix.append(row)

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    row_len = x2 - x1 + 1

    total = 0
    for i in range(row_len):
        if y1 - 2 < 0:  # [-1] 되어버리면 행렬의 맨마지막 열로 돌아오기에, 이 부분 따로 처리해주기
            total += matrix[x1 - 1 + i][y2 - 1]
        else:
            total += matrix[x1 - 1 + i][y2 - 1] - matrix[x1 - 1 + i][y1 - 2]

    print(total)
