# git commit -m "submit : BOJ 02448 별 찍기 - 11 (eonyong)"
def stars(row, col, n, boards):
    if not n:
        return
    else:
        if boards[row][col] == ' ' and not row % 3:
            boards[row][col] = '*'
            boards[row + 1][col - 1: col + 2] = '* *'
            boards[row + 2][col - 2: col + 3] = '*' * 5

            while n:
                stars(row + (n >> 1), col + (n >> 1), (n >> 1), boards)
                stars(row + (n >> 1), col - (n >> 1), (n >> 1), boards)
                n >>= 1


n = int(input())
boards = [[' '] * (2 * n - 1) for _ in range(n)]
stars(0, n - 1, n, boards)
for board in boards:
    print(''.join(board))
