# git commit -m "submit : BOJ 09095 1, 2, 3 더하기 (changjun)"

t = int(input())
lst = [int(input()) for _ in range(t)]

max_num = max(lst)

res = [0]*(max_num+1)
res[1] = 1
res[2] = 1 + 1
res[3] = 1 + 2 + 1
for i in range(4, max_num+1):
    res[i] = res[i-1]+ res[i-2] + res[i-3]

for i in lst:
    print(res[i])