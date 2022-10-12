# git commit -m "submit : BOJ 23291 어항 정리 (yoonseok)"
N, K = map(int,input().split())
fishbowls = [[0]*N for _ in range(N)]
fishbowls[0] = list(map(int,input().split()))
height = 1
width = 1
start = 0
def step1():
    target = min(fishbowls[0])
    for i in range(N):
        if fishbowls[0][i]==target:
            fishbowls[0][i] +=1
def step2():
    global height
    global width
    global start
    height = 1
    width = 1
    start = 0
    turn = 1
    while start+width+height <= N:
        
        for i in range(height):
            for j in range(width):
                ni = width-j
                nj = i+width+start
                fishbowls[ni][nj]=fishbowls[i][j+start]
                fishbowls[i][j+start]=0
        start+=width
        if turn%2:
            height+=1
        else:
            width+=1
        turn+=1
def step3():
    dx = [-1,0,1,0]
    dy = [0,-1,0,1]
    send = [[[0]*4 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if fishbowls[i][j] == 0:
                continue
            for k in range(4):
                ni = i+dx[k]
                nj = j+dy[k]
                if ni < 0 or nj <0 or ni>=N or nj>=N:
                    continue
                if fishbowls[ni][nj]>fishbowls[i][j]:
                    continue
                if fishbowls[ni][nj]==0:
                    continue
                send[i][j][k] = (fishbowls[i][j]-fishbowls[ni][nj])//5
    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i+dx[k]
                nj = j+dy[k]
                if ni < 0 or nj <0 or ni>=N or nj>=N:
                    continue
                fishbowls[i][j]-=send[i][j][k]
                fishbowls[ni][nj]+=send[i][j][k]

def step4():
    global height
    global width
    global start
    for i in range(start+width):
        fishbowls[0][i] = fishbowls[i%height][i//height+start]
        
        fishbowls[i%height][i//height+start]=0

def step5():
    for i in range(N//2):
        fishbowls[1][N-i-1] = fishbowls[0][i]
        fishbowls[0][i]=0
    for i in range(2):
        for j in range(N//4):
            fishbowls[i+2][j+N//4*3]=fishbowls[2-i-1][N//4*3-j-1]
            fishbowls[2-i-1][N//4*3-j-1]=0
            # print(i+2,j+N//4*3,2-i-1,N//4*2-j-1)
def step6():
    k = 0
    for i in range(N//4):
        for j in range(4):
            fishbowls[0][k] = fishbowls[j][i+N//4*3]
            fishbowls[j][i+N//4*3]=0
            k+=1
count = 0
while max(fishbowls[0])-min(fishbowls[0])>K: 
    # print("-----------------------------")
    step1()
    # print("1")
    # for i in range(N-1,-1,-1):
    #     print(fishbowls[i])
    step2()
    # print("2")
    # for i in range(N-1,-1,-1):
    #     print(fishbowls[i])
    step3()
    # print("3")
    # for i in range(N-1,-1,-1):
    #     print(fishbowls[i])
    step4()
    # print("4")
    # for i in range(N-1,-1,-1):
    #     print(fishbowls[i])
    step5()
    # print("5")
    # for i in range(N-1,-1,-1):
    #     print(fishbowls[i])
    step3()
    # print("6")
    # for i in range(N-1,-1,-1):
    #     print(fishbowls[i])
    step6()
    # print("7")
    # for i in range(N-1,-1,-1):
    #     print(fishbowls[i])
    count+=1
    # print("aasd")
    # print(fishbowls[0])
    
    # print(max(fishbowls[0]),min(fishbowls[0]))
    # print("-----------------------------")

print(count)
