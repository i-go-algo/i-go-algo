# git commit -m "submit : BOJ 02239 스도쿠 (eonyong)"
import sys

input = sys.stdin.readline


def RemainNum(row, col, board, n):
    for j in range(9):
        if n in [board[j][col], board[row][j]]:
            return False

    for nj in range((row // 3) * 3, (row // 3 + 1) * 3):
        for ni in range((col // 3) * 3, (col // 3 + 1) * 3):
            if n == board[nj][ni]:
                return False

    return True


def Sudoku(i, l, zeros, board):
    if i == l:
        for ans in [''.join(list(map(str, n))) for n in board]:
            print(ans)
        exit(0)
    else:
        r, c = zeros[i]
        for num in range(1, 10):
            if RemainNum(r, c, board, num):
                board[r][c] = num
                Sudoku(i + 1, l, zeros, board)
                board[r][c] = 0


boards = [list(map(int, list(input().strip()))) for _ in range(9)]
zeros = []

for row in range(9):
    for col in range(9):
        if not boards[row][col]:
            zeros.append((row, col))

Sudoku(0, len(zeros), zeros, boards)