# git commit -m "submit : BOJ 01932 정수 삼각형 (changjun)"

n = int(input())
lst = [list(map(int,input().split())) for _ in range(n)]

for i in range(1, len(lst)):
    lst[i][0] = lst[i][0] + lst[i-1][0]
    for j in range(1, i):
        lst[i][j] = lst[i][j] + max(lst[i-1][j-1], lst[i-1][j])
    lst[i][i] = lst[i][i] + lst[i-1][i-1]
print(max(lst[-1]))
