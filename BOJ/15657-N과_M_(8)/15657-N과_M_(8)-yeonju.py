def dfs(start):
    if len(nums) == m:
        print(' '.join(map(str, nums)))
        return

    for i in range(start, n):
        nums.append(li[i])
        dfs(i)
        nums.pop()


n, m = map(int, input().split())
li = sorted(list(map(int, input().split())))
nums = []
dfs(0)
