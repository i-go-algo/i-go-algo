def dfs(x, y, n):
    global minus_one, zero, one
    num_check = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != num_check:
                for k in range(3):
                    for l in range(3):
                        dfs(x + k * (n // 3), y + l * (n // 3), n // 3)
                return

    if num_check == -1:
        minus_one += 1
    elif num_check == 0:
        zero += 1
    else:
        one += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

minus_one = 0
zero = 0
one = 0

dfs(0, 0, n)

print(minus_one)
print(zero)
print(one)
