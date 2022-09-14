import sys
from collections import deque
input = sys.stdin.readline

# 상 우 하 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def move():
    direction = 1
    time = 1
    x, y = 0, 0
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 1

    while True:
        nx, ny = x + dx[direction], y + dy[direction]

        if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1:
            if arr[nx][ny] == 0:
                temp_x, temp_y = queue.popleft()
                arr[temp_x][temp_y] = 0

            arr[nx][ny] = 1
            queue.append((nx, ny))

            if time in times.keys():
                direction = turn(direction, times[time])

            time += 1
            x, y = nx, ny

        else:
            return time


n = int(input())
k = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(k):
    a, b = map(int, input().split())
    arr[a - 1][b - 1] = 2

l = int(input())
times = dict()

for _ in range(l):
    x, c = input().split()
    times[int(x)] = c

print(move())
