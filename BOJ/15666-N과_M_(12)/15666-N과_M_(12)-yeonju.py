def dfs(start):
    if len(temp) == m:
        print(' '.join(map(str, temp)))
        return

    for i in range(start, len(nums)):
        temp.append(nums[i])
        dfs(i)
        temp.pop()


n, m = map(int, input().split())
nums = sorted(set(list(map(int, input().split()))))
temp = []

dfs(0)


# git commit -m "submit : BOJ 15666 N과 M (12) (yeonju)"