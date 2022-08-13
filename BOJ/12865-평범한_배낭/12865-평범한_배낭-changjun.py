# # git commit -m "submit : BOJ 12865 평범한 배낭 (changjun)"

n, k = map(int,input().split())

lst = [list(map(int,input().split())) for _ in range(n)]
lst = [[0,0]] + lst
ans = [[0]*(k+1) for _ in range(n+1)]

for i in range(n+1):
    for j in range(k+1):
        if j >= lst[i][0]:
            ans[i][j] = max(ans[i-1][j], ans[i-1][j-lst[i][0]] + lst[i][1])
        else:
            ans[i][j] = ans[i-1][j]

print(ans[-1][-1])













# from collections import deque

# n, k = map(int,input().split())

# lst = [list(map(int,input().split())) for _ in range(n)]
# res = 0

# q = deque()

# for idx, value in enumerate(lst):
#     w, v = value
#     if w <= k:
#         q.append((idx, w, v))
#         res = max(res, v)
# while q:
#     my_idx, my_w, my_v = q.popleft()
#     for idx in range(my_idx+1, n):
#         w, v = lst[idx]
#         tmp_w = my_w + w
#         tmp_v = my_v + v
#         if  tmp_w <= k:
#             q.append((idx, tmp_w, tmp_v))
#             res = max(res, tmp_v)
# print(res)




