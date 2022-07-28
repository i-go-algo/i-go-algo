# git commit -m "submit : BOJ 01932 정수 삼각형 (eonyong)"
answer = 0
n = int(input())
boards = [list(map(int, input().split())) for _ in range(n)]

for row in range(1, n):
    for col in range(row + 1):
        if not col:
            boards[row][col] += boards[row - 1][col]
        elif col == row:
            boards[row][col] += boards[row - 1][col - 1]
        else:
            boards[row][col] += max(boards[row - 1][col], boards[row - 1][col - 1])
print(max(boards[-1]))
