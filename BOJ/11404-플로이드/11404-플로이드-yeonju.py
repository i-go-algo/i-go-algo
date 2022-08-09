import sys
input = sys.stdin.readline


def floyd_warshall():
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i != j and arr[i][j] > arr[i][k] + arr[k][j]:
                    arr[i][j] = arr[i][k] + arr[k][j]

    return arr


n = int(input())
m = int(input())
INF = sys.maxsize
arr = [[INF for _ in range(n)] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    if c < arr[a - 1][b - 1]:
        arr[a - 1][b - 1] = c

floyd_warshall()

for i in range(n):
    for j in range(n):
        if arr[i][j] == INF:
            print(0, end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
