# git commit -m "submit : BOJ 01149 RGB거리 (changjun)"

n = int(input())

lst = [list(map(int,input().split())) for _ in range(n)]

r, g, b = lst[0]

for x, y, z in lst[1:]:
    r, g, b = x + min(g,b), y + min(r,b), z + min(r,g)

print(min(r,g,b))
    
    



# ans = 1000*n


# def func(x, color, res):
#     global ans

#     res += lst[x][color]
#     if res > ans:
#         return

#     if x < n-1:
#         for k in range(3):
#             if k != color:
#                 func(x+1, k, res)
#     else:
#         ans = min(res, ans)


# for i in range(3):
#     func(0, i, 0)

# print(ans)