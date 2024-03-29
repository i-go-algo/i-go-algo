import sys
input = sys.stdin.readline


def check_row(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True


def check_col(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True


def check_square(r, c, num):
    nr = (r // 3) * 3
    nc = (c // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[nr + i][nc + j] == num:
                return False
    return True


def dfs(depth):
    if depth == len(zeros):
        for row in range(9):
            for col in range(9):
                print(board[row][col], end='')
            print()
        exit()

    nr, nc = zeros[depth]
    for num in range(1, 10):
        if check_row(nr, num) and check_col(nc, num) and check_square(nr, nc, num):
            board[nr][nc] = num
            dfs(depth + 1)
            board[nr][nc] = 0


board = []
zeros = []
for r in range(9):
    board.append(list(map(int, input().rstrip())))
    for c in range(9):
        if board[r][c] == 0:
            zeros.append((r, c))
dfs(0)
