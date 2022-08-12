# git commit -m "submit : BOJ 09465 스티커 (changjun)"

t = int(input())


for case in range(t):
    n = int(input())
    lst = [list(map(int, input().split())) for _ in range(2)]
    ans = [[0] * n for _ in range(2)]
    if n >= 2:
        ans[0][0] = lst[0][0]
        ans[1][0] = lst[1][0]
        ans[0][1] = lst[1][0] + lst[0][1]
        ans[1][1] = lst[0][0] + lst[1][1]

        for j in range(2, n):
            ans[0][j] = max(ans[1][j - 1], ans[1][j - 2]) + lst[0][j]
            ans[1][j] = max(ans[0][j - 1], ans[0][j - 2]) + lst[1][j]
        res = 0
        for i in range(2):
            for j in range(2):
                res = max(res, ans[i][-j - 1])

        print(res)
    else:
        print(max(lst[0][0], lst[1][0]))
# d_row = [1, 1]
# d_index = [1, 2]


# def func(row, index, num):

#     for d in range(2):
#         n_index = index + d_index[d]
#         if n_index < n:
#             n_row = (row + d_row[d]) % 2
#             func(n_row, n_index, num + lst[n_row][n_index])
#         else:
#             global ans
#             ans = max(ans, num)


# for case in range(t):
#     n = int(input())
#     lst = [list(map(int, input().split())) for _ in range(2)]
#     ans = 0

#     func(0, 0, lst[0][0])
#     func(1, 0, lst[1][0])
#     func(0, 1, lst[0][1])
#     func(1, 1, lst[1][1])
#     print(ans)

