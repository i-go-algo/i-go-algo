# git commit -m "submit : BOJ 17144 미세먼지 안녕! (eonyong)"
r, c, t = map(int, input().split())
boards = []
air_y, air_x = 0, 0
for row in range(r):
    line = list(map(int, input().split()))
    for col in range(c):
        if line[col] == -1:
            air_x, air_y = col, row
    boards.append(line[:])

for _ in range(t):
    virtualBoard = [[0] * c for _ in range(r)]
    for row in range(r):
        for col in range(c):
            virtualBoard[row][col] += boards[row][col]
            if boards[row][col] > 0:
                cnt, effect_boundary = 0, []
                for j, i in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    nj, ni = row + j, col + i
                    if 0 <= nj < r and 0 <= ni < c and boards[nj][ni] != -1:
                        cnt += 1
                        effect_boundary.append([nj, ni])
                dust = boards[row][col] // 5
                for y, x in effect_boundary:
                    virtualBoard[row][col] -= dust
                    virtualBoard[y][x] += dust

    for d in range(air_y - 2, air_y + 2):
        if 0 <= d < r:
            virtualBoard[d][0] = 0

    for idx in range(air_y - 1, 0, -1):
        virtualBoard[idx][0], virtualBoard[idx - 1][0] = virtualBoard[idx - 1][0], virtualBoard[idx][0]
    for idx in range(c - 1):
        virtualBoard[0][idx], virtualBoard[0][idx + 1] = virtualBoard[0][idx + 1], virtualBoard[0][idx]
    for idx in range(air_y - 1):
        virtualBoard[idx][c - 1], virtualBoard[idx + 1][c - 1] = virtualBoard[idx + 1][c - 1], virtualBoard[idx][c - 1]
    for idx in range(c - 1, 0, -1):
        virtualBoard[air_y - 1][idx], virtualBoard[air_y - 1][idx - 1] = virtualBoard[air_y - 1][idx - 1], virtualBoard[air_y - 1][idx]

    for idx in range(air_y, r - 1):
        virtualBoard[idx][0], virtualBoard[idx + 1][0] = virtualBoard[idx + 1][0], virtualBoard[idx][0]
    for idx in range(c - 1):
        virtualBoard[r - 1][idx], virtualBoard[r - 1][idx + 1] = virtualBoard[r - 1][idx + 1], virtualBoard[r - 1][idx]
~    for idx in range(r - 1, air_y, -1):
        virtualBoard[idx][c - 1], virtualBoard[idx - 1][c - 1] = virtualBoard[idx - 1][c - 1], virtualBoard[idx][c - 1]
    for idx in range(c - 1, 0, -1):
        virtualBoard[air_y][idx], virtualBoard[air_y][idx - 1] = virtualBoard[air_y][idx - 1], virtualBoard[air_y][idx]

    boards = virtualBoard[:]
print(sum(map(sum, boards)))