from collections import deque, defaultdict


def bfs(start, end):
    global ans
    queue = deque()
    queue.append(start)
    visited[start] = 1

    while queue:
        cur_value = queue.popleft()

        if cur_value == end:
            ans = visited[cur_value]
            return

        calculation2 = int(str(cur_value) + '1')

        for next_value in [cur_value * 2, calculation2]:
            if not visited[next_value] and next_value <= 10 ** 9:
                queue.append(next_value)
                visited[next_value] = visited[cur_value] + 1
    ans = -1
    return


a, b = map(int, input().split())
visited = defaultdict(int)
ans = 0
bfs(a, b)

print(ans)
