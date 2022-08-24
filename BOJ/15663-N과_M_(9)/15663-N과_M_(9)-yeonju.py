def dfs():
    if len(temp) == m:
        print(' '.join(map(str, temp)))
        return

    prev = 0
    for i in range(0, n):
        if visited[i] == 0 and prev != nums[i]:
            visited[i] = 1
            temp.append(nums[i])
            prev = nums[i]
            dfs()
            visited[i] = 0
            temp.pop()


n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []
visited = [0 for _ in range(n)]

dfs()
