import sys
from collections import defaultdict, deque
input = sys.stdin.readline

for _ in range(int(input())):
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    result = times[::]
    indegree = [0] * n
    arr = defaultdict(list)

    for _ in range(k):
        a, b = map(int, input().split())
        arr[a - 1].append(b - 1)
        indegree[b - 1] += 1

    w = int(input()) - 1

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    while queue:
        now = queue.popleft()
        for i in arr[now]:
            indegree[i] -= 1
            result[i] = max(result[i], result[now] + times[i])
            if indegree[i] == 0:
                queue.append(i)
                if i == w:
                    break
    print(result[w])
