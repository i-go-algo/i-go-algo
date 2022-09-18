import sys
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
graph = []
visited = [[0 for _ in range(m)] for _ in range(n)]
r, c, direction = map(int, input().split())

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited[r][c] = 1
cnt = 1

while True:
    for _ in range(4):
        direction = (direction - 1) % 4
        nx = r + dx[direction]
        ny = c + dy[direction]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            if visited[nx][ny] == 0:
                visited[nx][ny] = 1
                cnt += 1
                r = nx
                c = ny
                break

    else:
        if graph[r - dx[direction]][c - dy[direction]] == 1:
            print(cnt)
            exit()
        else:
            r, c = r - dx[direction], c - dy[direction]
            