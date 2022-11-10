# git commit -m "submit : BOJ 01005 ACM Craft (yoonseok)"
from collections import deque
for _ in range(int(input())):
    N,K = map(int,input().split())
    D = list(map(int,input().split()))
    arr = [[] for _ in range(N+1)]
    degree = [0 for _ in range(N+1)]
    depth = [0 for _ in range(N + 1)]
    for _ in range(K):
        x,y = map(int,input().split())
        arr[x].append(y)
        degree[y] += 1
    W = int(input())
    queue = deque()
    for i in range(1, N+1):
        if degree[i] == 0:
            queue.append(i)
            depth[i] = D[i-1]
    while queue and degree[W] != 0:
        x = queue.popleft()
        for n in arr[x]:
            degree[n] -= 1
            depth[n] = max(depth[x]+ D[n-1], depth[n])
            if degree[n] == 0:
                queue.append(n)
    print(depth[W])