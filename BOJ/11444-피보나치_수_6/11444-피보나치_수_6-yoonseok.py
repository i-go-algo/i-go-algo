# git commit -m "submit : BOJ 11444 피보나치 수 6 (yoonseok)"
n = int(input())
lst = [[1, 1],[1, 0]]


def matmul(lst1, lst2):
    ans = [[0] * 2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            tmp = 0
            for k in range(2):
                tmp += lst1[i][k] * lst2[k][j]
            ans[i][j] = tmp % 1000000007
    return ans


def func(input_lst, x):
    if x == 1:
        for i in range(2):
            for j in range(2):
                input_lst[i][j] = input_lst[i][j] % 1000000007
        return input_lst

    elif x % 2 == 0:
        tmp = func(input_lst, x // 2)
        return matmul(tmp, tmp)
    else:
        tmp = func(input_lst, x // 2)
        return matmul(matmul(tmp, tmp), lst)


ans = func(lst, n)

print(ans[1][0])