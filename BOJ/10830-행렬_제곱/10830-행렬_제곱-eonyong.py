# git commit -m "submit : BOJ 10830 행렬 제곱 (eonyong)"
from collections import defaultdict


def matrixSquare(n, a, b):
    squares = [[0] * n for _ in range(n)]
    for i in range(n):
        for row in range(n):
            total = 0
            for col in range(n):
                total += a[i][col] * b[col][row]
            squares[i][row] = total % 1000
    return squares


def powerPower(b, pwd):
    i = 1
    while i != b:
        if i * 2 <= b:
            pwd[2 * i] = matrixSquare(n, pwd[i], pwd[i])
            i *= 2
        else:
            for j in reversed(pwd.keys()):
                if i + j <= b:
                    pwd[i + j] = matrixSquare(n, pwd[i], pwd[j])
                    i += j
                    break
    else:
        return pwd[b]


n, b = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
pwd = defaultdict(list)

for row in range(n):
    for col in range(n):
        matrix[row][col] %= 1000

pwd[1] = matrix


for p in powerPower(b, pwd):
    print(*p)