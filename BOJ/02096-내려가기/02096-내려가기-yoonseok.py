# git commit -m "submit : BOJ 02096 내려가기 (yoonseok)"
N = int(input())

max_stair = [0,0,0]
min_stair = [0,0,0]

for i in range(0,N):
    stair = list(map(int,input().split()))
    max_t = max_stair[:]
    min_t = min_stair[:]
    max_stair[0] = max(stair[0]+max_t[0], stair[0]+max_t[1])
    max_stair[1] = max(stair[1]+max_t[0], stair[1]+max_t[1], stair[1]+max_t[2])
    max_stair[2] = max(stair[2]+max_t[1], stair[2]+max_t[2])
    min_stair[0] = min(stair[0]+min_t[0], stair[0]+min_t[1])
    min_stair[1] = min(stair[1]+min_t[0], stair[1]+min_t[1], stair[1]+min_t[2])
    min_stair[2] = min(stair[2]+min_t[1], stair[2]+min_t[2])

print(max(max_stair), min(min_stair))
