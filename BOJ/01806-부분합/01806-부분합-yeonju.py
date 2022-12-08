n, s = map(int, input().split())
nums = list(map(int, input().split()))

start, end = 0, 0
total = nums[0]
ans = 1000000

while True:
    if total < s:
        end += 1
        if end == n:
            break
        total += nums[end]

    elif total >= s:
        total -= nums[start]
        ans = min(ans, end - start + 1)
        start += 1

print(0 if ans == 100000 else ans)
