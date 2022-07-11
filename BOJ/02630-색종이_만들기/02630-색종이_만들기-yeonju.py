def dfs(x, y, n):
    global white, blue
    color_check = arr[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != color_check:
                for k in range(2):
                    for l in range(2):
                        dfs(x + k * (n // 2), y + l * (n // 2), n // 2)
                return

    if color_check == 0:
        white += 1
    else:
        blue += 1


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

white = 0
blue = 0

dfs(0, 0, n)

print(white)
print(blue)
