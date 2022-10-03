# git commit -m "submit : BOJ 17825 주사위 윷놀이 (yoonseok)"
nums = list(map(int,input().split()))
lines = [list(2*x for x in range(21))+[0],
    list(10+3*x for x in range(4))+list(25+5*x for x in range(4))+[0],
    list(20+2*x for x in range(3))+list(25+5*x for x in range(4))+[0],
    [30]+list(28-x for x in range(3))+list(25+5*x for x in range(4))+[0]]

tokens = [[0,0] for i in range(4)]
#print(lines)
answer = 0

def dfs(sums,tokens,ind):
    global answer
    if ind == 10:
        answer = max(answer,sums)
        return
    for i in range(4):
        line = tokens[i][0]
        next_line = line
        now_loc = tokens[i][1]
        line_end = len(lines[tokens[i][0]])
        if(now_loc==line_end-1):
            continue
        next_loc = min(now_loc+nums[ind],line_end-1)
        if line==0 and next_loc%5==0 and next_loc < 20:#파란색 화살표인 지점
            next_line = next_loc//5
            next_loc = 0
        
        if next_loc==line_end-2:#40점인지점
            next_line = 0
            next_loc = 20
        if next_line!=0 and next_loc !=0:
            if lines[next_line][next_loc]==25:
                next_line=1
                next_loc = 4
            elif lines[next_line][next_loc]==30:
                next_line=1
                next_loc = 5
            elif lines[next_line][next_loc]==35:
                next_line = 1
                next_loc = 6
        for j in range(4):
            #print(tokens[j],next_loc,next_line,now_loc,line, nums[ind])
            if next_loc==len(lines[next_line])-1:
                continue
            if j==i:
                continue
            if next_loc==tokens[j][1] and next_line==tokens[j][0]:
                break
        else:
            tokens[i][0] = next_line
            tokens[i][1] = next_loc
            
            #print(tokens[i])
            dfs(sums+lines[next_line][next_loc],tokens,ind+1)
        tokens[i][0] = line
        tokens[i][1] = now_loc
dfs(0,tokens,0)
print(answer)