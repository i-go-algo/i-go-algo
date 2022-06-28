# git commit -m "submit : BOJ 01012 유기농 배추 (yoonseok)"
from queue import Queue

dx = [0,1,0,-1]
dy = [1,0,-1,0]
T = int(input())
for tc in range(T):
    answer = 0
    M, N, K = map(int,input().split())
    farm = [[0]*M for i in range(N)]
    for i in range(K):
        x,y = map(int,input().split())
        farm[y][x]=1
    checked = [[False]*M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if checked[i][j]:
                continue
            if farm[i][j]==0:
                continue
            answer+=1
            print(i,j,"aaaa")
            checked[i][j]=True
            Q = Queue()
            Q.put((i,j))
            while (not Q.empty()):
                x,y = Q.get()
                for k in range(4):
                    ni = x+dx[k]
                    nj = y+dy[k]
                    if ni<0 or ni >= N or nj<0 or nj >= M:
                        continue
                    if checked[ni][nj]:
                        continue
                    if farm[ni][nj]==0:
                        continue
                    checked[ni][nj]=True
                    Q.put((ni,nj))
                    
    print(answer)