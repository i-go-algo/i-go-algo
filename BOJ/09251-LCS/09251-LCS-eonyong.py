# git commit -m "submit : BOJ 09251 LCS (eonyong)"
def LCS(a, b):
    a, b = ' ' + a, ' ' + b
    n, m = len(a), len(b)
    c = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            c[i][j] = c[i - 1][j - 1] + 1 if a[i] == b[j] else max(c[i - 1][j], c[i][j - 1])
    return max(max(c))

print(LCS(*[input() for _ in range(2)]))
