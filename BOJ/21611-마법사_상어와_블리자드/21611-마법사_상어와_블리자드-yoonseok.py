# git commit -m "submit : BOJ 21611 마법사 상어와 블리자드 (yoonseok)"
dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [-1, -1, 0, 1, 1, 1, 0, -1]

shark_dx = [-1, 0, 1, 0]
shark_dy = [0, -1, 0, 1]

m, s = map(int, input().split()) 
fish = [[[[], []] for _ in range(4)] for _ in range(4)]
fish_smell = [[0] * 4 for _ in range(4)]

for _ in range(m) :
    x, y, d = map(int, input().split()) 
    fish[x-1][y-1][0].append(d-1)

x, y = map(int, input().split()) 
x -= 1
y -= 1 
path = []
max_fish_count = -1

visited = [[False] * 4 for _ in range(4)]

def copy_start() :
    for i in range(4) :
        for j in range(4) :
            for dir in fish[i][j][0] :
                fish[i][j][1].append(dir)

def move_fish() :
    position = []
    for i in range(4) :
        for j in range(4) :
            while fish[i][j][0] :
                nd = fish[i][j][0].pop()
                flag = False
                for _ in range(8) : 
                    nx = i + dx[nd]
                    ny = j + dy[nd]

                    if 0 <= nx < 4 and 0 <= ny < 4 and fish_smell[nx][ny] == 0 and not (nx == x and ny == y) :
                        position.append((nx, ny, nd))
                        flag = True
                        break

                    nd = (nd - 1) % 8
                if flag == False :
                    position.append((i, j, nd))
    return position

def select_move_shark(r, c, fish_count, move_count, temp_path) :
    global x, y, visited, max_fish_count, path
    if move_count == 3 : 
        if max_fish_count < fish_count :
            max_fish_count = fish_count
            path = [d for d in temp_path]
        return

    for d in range(4) :
        nx = r + shark_dx[d]
        ny = c + shark_dy[d]
        if 0 <= nx < 4 and 0 <= ny < 4 :
            if not visited[nx][ny] :
                visited[nx][ny] = True 
                next_fish_count = fish_count + len(fish[nx][ny][0])
                select_move_shark(nx, ny, next_fish_count, move_count+1, temp_path+[d])
                visited[nx][ny] = False
            else :
                select_move_shark(nx, ny, fish_count, move_count+1, temp_path+[d])

def move_shark() :
    global x, y, fish, fish_smell
    for d in path :
        x = x + shark_dx[d]
        y = y + shark_dy[d]
        if fish[x][y][0] :
            fish[x][y][0] = []
            fish_smell[x][y] = 3 

def reduce_smell() :
    global fish_smell
    for i in range(4) :
        for j in range(4) :
            if fish_smell[i][j] > 0 :
                fish_smell[i][j] -= 1

def copy_end() :
    global fish
    for i in range(4) :
        for j in range(4) :
            while fish[i][j][1] :
                fish[i][j][0].append(fish[i][j][1].pop())

for now in range(s) :

    copy_start()

    position = move_fish()
    for r, c, dir in position :
        fish[r][c][0].append(dir)

    path = []
    max_fish_count = -1


    select_move_shark(x, y, 0, 0, [])
    move_shark()

    reduce_smell()

    copy_end()

result = 0
for i in range(4) :
    for j in range(4) :
        result += len(fish[i][j][0])

print(result)