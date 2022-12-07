# deque 쓰면 시간 초과 나네요,,, 

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(x, y, alphabet):
    ans = 1
    queue = set([(x, y, alphabet)])

    while queue:
        x, y, alphabet = queue.pop()
        ans = max(ans, len(alphabet))

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if arr[nx][ny] not in alphabet:
                    queue.add((nx, ny, alphabet + arr[nx][ny]))
    return ans


r, c = map(int, input().split())
arr = [list(input()) for _ in range(r)]

print(bfs(0, 0, arr[0][0]))
