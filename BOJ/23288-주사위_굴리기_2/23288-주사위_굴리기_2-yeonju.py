import sys
from collections import deque
input = sys.stdin.readline

# 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def move(x, y, direction):
    nx = x + dx[direction]
    ny = y + dy[direction]

    if 0 <= nx < n and 0 <= ny < m:
        pass
    else:
        if direction in (0, 2):
            direction += 1
        elif direction in (1, 3):
            direction -= 1

        nx = x + dx[direction]
        ny = y + dy[direction]

    return nx, ny, direction


def roll_dice(dice, new_direction):
    # 오른쪽
    if new_direction == 0:
        dice = {'up': dice['up'], 'left': dice['bottom'], 'top': dice['left'], 'right': dice['top'], 'down': dice['down'], 'bottom': dice['right']}
    # 왼쪽
    elif new_direction == 1:
        dice = {'up': dice['up'], 'left': dice['top'], 'top': dice['right'], 'right': dice['bottom'],
                'down': dice['down'], 'bottom': dice['left']}
    # 아래로
    elif new_direction == 2:
        dice = {'up': dice['bottom'], 'left': dice['left'], 'top': dice['up'], 'right': dice['right'],
                'down': dice['top'], 'bottom': dice['down']}
    # 위로
    else:
        dice = {'up': dice['top'], 'left': dice['left'], 'top': dice['down'], 'right': dice['right'],
                'down': dice['bottom'], 'bottom': dice['up']}

    return dice


def count_score(b, new_x, new_y):
    c = 1
    visited = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque()
    queue.append((new_x, new_y))
    visited[new_x][new_y] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if arr[nx][ny] == b and visited[nx][ny] != 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    c += 1
    return b * c


def compare_direction(a, b, new_direction):
    if a > b:
        if new_direction == 0: new_direction = 2
        elif new_direction == 1: new_direction = 3
        elif new_direction == 2: new_direction = 1
        else: new_direction = 0

    elif a < b:
        if new_direction == 0:
            new_direction = 3
        elif new_direction == 1:
            new_direction = 2
        elif new_direction == 2:
            new_direction = 0
        else:
            new_direction = 1

    return new_direction


n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
x, y = 0, 0
direction = 0
dice = {'up': 2, 'left': 4, 'top': 1, 'right': 3, 'down': 5, 'bottom': 6}
score = 0

# 점이 이동하는 함수
for i in range(k):
    new_x, new_y, new_direction = move(x, y, direction)

# 이동한 후 주사위가 굴러가는 함수
    new_dice = roll_dice(dice, new_direction)

# 점수 획득하는 함수
    b = arr[new_x][new_y]
    score += count_score(b, new_x, new_y)

# 비교하는 함수
    a = new_dice['bottom']
    new_direction = compare_direction(a, b, new_direction)
    x, y, direction, dice = new_x, new_y, new_direction, new_dice

print(score)
