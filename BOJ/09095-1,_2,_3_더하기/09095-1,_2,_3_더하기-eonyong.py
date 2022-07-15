# git commit -m "submit : BOJ 09095 1, 2, 3 더하기 (eonyong)"

def cntSum(m, number):
    global cnt
    if number == m:
        cnt += 1
    elif number < m:
        for i in [1, 2, 3]:
            cntSum(m, number + i)


n = int(input())
boards = [int(input()) for _ in range(n)]
for board in boards:
    cnt = 0
    cntSum(board, 0)
    print(cnt)