def nqueen(queen, row):
    global res
 
    if n == row:
        res += 1
        return 
 
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row] or abs(queen[row] - queen[i])== row - i:
                break
        else:
            nqueen(queen, row + 1)
 

n = int(input())
res = 0
nqueen([0] * n, 0)
print(res)

