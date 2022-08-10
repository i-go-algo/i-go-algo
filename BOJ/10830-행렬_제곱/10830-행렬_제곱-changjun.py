# git commit -m "submit : BOJ 10830 행렬 제곱 (changjun)"

n, x = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]


def matmul(lst1, lst2):
    ans = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            tmp = 0
            for k in range(n):
                tmp += lst1[i][k] * lst2[k][j]
            ans[i][j] = tmp % 1000
    return ans


def func(input_lst, x):
    if x == 1:
        for i in range(n):
            for j in range(n):
                input_lst[i][j] = input_lst[i][j] % 1000
        return input_lst

    elif x % 2 == 0:
        tmp = func(input_lst, x // 2)
        return matmul(tmp, tmp)
    else:
        tmp = func(input_lst, x // 2)
        return matmul(matmul(tmp, tmp), lst)


ans = func(lst, x)

for line in ans:
    print(*line)
