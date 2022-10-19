# git commit -m "submit : BOJ 23290 마법사 상어와 복제 (eonyong)"
import sys

input = sys.stdin.readline

# 물고기 이동 방향
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]

# 상어 이동방향
s_dr = [-1, 0, 1, 0]
s_dc = [0, -1, 0, 1]


# 상어 이동 dfs
def SharkShock(i, row, col, copies, bowls, c, route, directions):
    global routes
    # 3번의 움직임이 완료되면 routes에 루트, 이동 방향, 먹은 물고기 수 저장
    if i == 3:
        routes.append([route, directions, c])
    else:
        # 4방향으로 회전하며 이동
        for idx in range(4):
            nj, ni = row + s_dr[idx], col + s_dc[idx]
            if 0 <= nj < 4 and 0 <= ni < 4:
                # 한 번 방문한 곳은 물고기를 잡지 않고, 처음 방문한 곳은 물고기 수만틈 잡아먹는다.
                if not visited[nj][ni]:
                    visited[nj][ni] = True
                    SharkShock(i + 1, nj, ni, copies, bowls, c + bowls[nj][ni], route + [[nj, ni]], directions + [idx])
                    visited[nj][ni] = False
                else:
                    SharkShock(i + 1, nj, ni, copies, bowls, c, route + [[nj, ni]], directions + [idx])


# 잡힌 물고기의 냄새를 저장할 공간
smells = [[0 for _ in range(4)] for _ in range(4)]
m, s = map(int, input().split())
# 존재하는 물고기의 [위치, 바라보는 방향] 저장
fishes = []

# 물고기 저장
for _ in range(m):
    fy, fx, d = map(int, input().split())
    fishes.append([fy - 1, fx - 1, d - 1])

# 상어 위치 저장
sy, sx = map(int, input().split())
sy, sx = sy - 1, sx - 1

answer = 0

for _ in range(s):
    # 물고기 복제
    copy_fishes = []
    for y, x, d in fishes:
        for i in range(8):
            nj, ni = y + dr[(d - i) % 8], x + dc[(d - i) % 8]
            if 0 <= nj < 4 and 0 <= ni < 4 and not smells[nj][ni] and (nj != sy or ni != sx):
                copy_fishes.append([nj, ni, (d - i) % 8])
                break
        else:
            copy_fishes.append([y, x, d])
    
    # 위치 별 복제된 물고기의 수 저장할 리스트
    bowls = [[0 for _ in range(4)] for _ in range(4)]
    for y, x, _ in copy_fishes:
        bowls[y][x] += 1

    # 상어의 이동 경로와 잡은 물고기 수 저장할 리스트
    routes = []
    visited = [[False for _ in range(4)] for _ in range(4)]
    SharkShock(0, sy, sx, copy_fishes, bowls, 0, [], [])
    # 잡아먹은 물고기 수, 이동방향에 대한 우선순위 순으로 정렬 후 가장 앞서 있는 값만 저장
    routes = sorted(routes, key=lambda x: (-x[2], x[1]))[0]

    # 복제된 물고기가 상어의 이동경로에 있으면 smell을 업데이트하고, 없으면 존재하는 물고기 리스트에 추가
    while copy_fishes:
        row, col, direction = copy_fishes.pop()
        if [row, col] not in routes[0]:
            fishes.append([row, col, direction])
        else:
            smells[row][col] = -3

    # 남아있는 냄새가 있는 구역의 값을 +1
    for row in range(4):
        for col in range(4):
            # 냄새가 남아있는 지역에 +1 을 해준다
            if smells[row][col] < 0:
                smells[row][col] += 1
    # 상어 위치 업데이트
    sy, sx = routes[0][-1]
    
print(len(fishes))
