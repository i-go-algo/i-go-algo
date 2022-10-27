# git commit -m "submit : BOJ 14891 톱니바퀴 (yoonseok)"
# 제일 위에 있는 자석이 [0] 오른쪽은 [2] 왼쪽은[6]

magnet = []
for i in range(4):
    magnet.append(list(map(int,input())))
n = int(input())
ind = [0,0,0,0]
stick = [False,False,False,False]
for i in range(n):
    rotate = list(map(int,input().split()))
    now = rotate[0]-1
    stick[now]=True
    for j in range(now-1,-1,-1) :
        if magnet[j][(2-ind[j])%8]!=magnet[j+1][(6-ind[j+1])%8] :
            stick[j] = stick[j+1]
    for j in range(now+1,4) :
        if magnet[j][(6-ind[j])%8]!=magnet[j-1][(2-ind[j-1])%8]:
            stick[j] = stick[j-1]
    for j in range(4):
        if stick[j] :
            ind[j] += rotate[1]*(-1)**(abs(j-now))
    for j in range(4):
        stick[j] = False
sum = 0
for i in range(4) :
    sum += magnet[i][(-ind[i])%8]*2**(i)
print(sum)


        

