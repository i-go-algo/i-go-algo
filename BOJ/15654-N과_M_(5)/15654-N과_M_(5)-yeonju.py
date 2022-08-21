def dfs():
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return

    for i in range(0, n):
        if li[i] not in nums:
            nums.append(li[i])
            dfs()
            nums.pop()


n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))
nums = []
dfs()
