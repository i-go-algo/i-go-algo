# git commit -m "submit : BOJ 14503 로봇 청소기 (yoonseok)"
N, M = map(int,input().split())
field_check = [[0]*M for i in range(N)]
x,y,dir = map(int,input().split())
field_check[x][y]=1
field = []
for i in range(N):
    field.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def turn_left():
    global dir
    dir-=1
    if dir == -1:
        dir = 3
cnt = 1
turn_time = 0
while True:
    turn_left()
    nx = x+dx[dir]
    ny = y+dy[dir]
    if field_check[nx][ny]==0 and field[nx][ny]==0:
        field_check[nx][ny]= 1
        cnt+=1
        x,y = nx,ny
        turn_time=0
        continue
    else:
        turn_time+=1
    if turn_time==4:
        nx= x-dx[dir]
        ny= y-dy[dir]
        if field[nx][ny]==0:
            x,y = nx,ny
        else:
            break
        turn_time = 0
print(cnt)