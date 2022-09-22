# git commit -m "submit : BOJ 15683 감시 (yoonseok)"
import copy

N, M = map(int, input().split())
cctv = []
room = []
for i in range(N):
    data = list(map(int, input().split()))
    room.append(data)
    for j in range(M):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])
c_num = len(cctv)

dx = [0, 0, -1, 0, 1]
dy = [0, 1, 0, -1, 0]

mode = [[],
        [[1], [2], [3], [4]],
        [[1, 3], [2, 4]],
        [[1, 2], [2, 3], [3, 4], [4, 1]],
        [[1, 2, 3], [1, 2, 4], [2, 3, 4], [1, 3, 4]],
        [[1, 2, 3, 4]],
        ]
min_not = 1000000000

def search(room, x, y, see):
    for look in see:
        nx = x
        ny = y
        while True:
            nx = nx + dx[look]
            ny = ny + dy[look]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                break
            if room[nx][ny] == 6:
                break
            room[nx][ny] = 7


def not_see():
    global min_not
    tmp_not = 0
    for x in range(N):
        for y in range(M):
            if room[x][y] == 0:
                tmp_not += 1
    min_not = min(min_not, tmp_not)

def dfs(depth):
    global c_num
    global room
    if depth == c_num:
        not_see()
        return

    m = cctv[depth][0]
    now_mode = mode[m]
    n_x, n_y = cctv[depth][1], cctv[depth][2]
    tmp_room = copy.deepcopy(room)
    for see in range(len(now_mode)):
        search(room, n_x, n_y, now_mode[see])
        dfs(depth + 1)
        room = copy.deepcopy(tmp_room)


dfs(0)
print(min_not)