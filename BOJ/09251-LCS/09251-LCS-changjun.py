# git commit -m "submit : BOJ 09251 LCS (changjun)"

a = input()
b = input()

lst = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            lst[i + 1][j + 1] = lst[i][j] + 1
        else:
            lst[i + 1][j + 1] = max(lst[i + 1][j], lst[i][j + 1])

print(lst[-1][-1])
