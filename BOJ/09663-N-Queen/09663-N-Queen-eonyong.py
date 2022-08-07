# git commit -m "submit : BOJ 09663 N-Queen (eonyong)"
def nQueen(r, n, row):
    global answer
    if r == n:
        answer += 1
    else:
        for c in range(n):
            row[r] = c
            if isCheck(r, row):
                nQueen(r + 1, n, row)


def isCheck(c, row):
    for i in range(c):
        if row[c] == row[i] or abs(row[c] - row[i]) == c - i:
            return False
    return True


global answer
answer = 0
n = int(input())
row = [0] * n
nQueen(0, n, row)
print(answer)
