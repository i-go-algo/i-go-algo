from collections import deque


def find_sibling():
    global cnt
    queue = deque([n])
    dist[n] = 0

    while queue:
        now = queue.popleft()

        if now == k:
            cnt += 1

        for next_place in [now - 1, now + 1, now * 2]:
            if 0 <= next_place <= 100000:
                if dist[next_place] == -1 or dist[next_place] == dist[now] + 1:
                    dist[next_place] = dist[now] + 1
                    queue.append(next_place)
    return


n, k = map(int, input().split())
dist = [-1 for _ in range(100001)]
cnt = 0

find_sibling()
print(dist[k])
print(cnt)
