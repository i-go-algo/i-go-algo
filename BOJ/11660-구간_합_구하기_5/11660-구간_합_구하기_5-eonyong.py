# git commit -m "submit : BOJ 11660 구간 합 구하기 5 (eonyong)"
from sys import stdin

n, m = map(int, stdin.readline().split())

boards = [[0] * (n + 1) for _ in range(n + 1)]

for row in range(1, n + 1):
    board = [0] + list(map(int, stdin.readline().split()))
    for col in range(1, n + 1):
        board[col] += board[col - 1]
        boards[row][col] = board[col] + boards[row - 1][col]

for _ in range(m):
    r1, c1, r2, c2 = map(int, stdin.readline().split())
    print(boards[r2][c2] - boards[r2][c1 - 1] - boards[r1 - 1][c2] + boards[r1 - 1][c1 - 1]) 