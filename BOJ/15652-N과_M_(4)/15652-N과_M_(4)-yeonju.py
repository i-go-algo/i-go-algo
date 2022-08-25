def dfs(start):
    for i in range(start, n + 1):
        if len(li) == m:
            print(' '.join(map(str, li)))
            return
        li.append(i)
        dfs(i)
        li.pop()


n, m = map(int, input().split())
li = []
dfs(1)
