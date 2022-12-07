from collections import defaultdict

t = int(input())
n = int(input())
a_nums = list(map(int, input().split()))
m = int(input())
b_nums = list(map(int, input().split()))

ans = 0
cnt_dict = defaultdict(int)

for i in range(n):
    for j in range(i, n):
        cnt_dict[sum(a_nums[i:j + 1])] += 1

for i in range(m):
    for j in range(i, m):
        ans += cnt_dict[t - sum(b_nums[i:j + 1])]

print(ans)
