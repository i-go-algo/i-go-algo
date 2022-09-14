# git commit -m "submit : BOJ 14888 연산자 끼워넣기 (yoonseok)"
N = int(input())
nums = list(map(int,input().split()))
opers = list(map(int,input().split()))
max_num = -(10**10)
min_num = 10**10
#print(nums)
#print(opers)
def dfs(i,res):
    if i == N-1:
        #print(opers)
        #print(res)
        global max_num
        global min_num
        #print(opers)
        max_num = max(max_num,res)
        min_num = min(min_num,res)
        return
    for k in range(4):
        if opers[k]==0:
            continue
        if k == 0:
            temp = res+nums[i+1]
        if k == 1:
            temp = res-nums[i+1]
        if k ==2:
            temp = res*nums[i+1]
        if k == 3:
            if res<0:
                temp = -(abs(res)//nums[i+1])
            else:
                temp = res//nums[i+1]
        opers[k]-=1
        dfs(i+1,temp)
        opers[k]+=1
dfs(0,nums[0])
print(max_num)
print(min_num)