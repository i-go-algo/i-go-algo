# git commit -m "submit : BOJ 09663 N-Queen (yoonseok)"
N = int(input())
q_loc = [-1]*N
count = 0
def dfs(ind):
    global count
    if ind == N:
        count+=1
        return
    for i in range(N):
        for k in range(ind):
            if i == q_loc[k]:
                break
            if abs(i-q_loc[k])==abs(k-ind):
                break
        else:
            if ind+1==N:
                count+=1
                return
            q_loc[ind]=i
            dfs(ind+1)
dfs(0)
print(count)