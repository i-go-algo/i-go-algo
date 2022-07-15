# git commit -m "submit : BOJ 01043 거짓말 (yoonseok)"
# 같은 파티에 참석하는 사람들끼리를 그래프로 연결해서 그래프 탐색을 통해 거짓말을 하면 안되는 파티들을 가려냄
# 그러기위해서 set을 사용했고 최종적으로 전체 파티의 수 - 거짓말 하면 안되는 파티의수 출력
from collections import deque
N, M = map(int,input().split())
know = list(map(int,input().split()))
links = [[0]*(N+1) for i in range(N+1)]
check = [False]*(1+N)
goParty = [set() for i in range(N+1)]
noTalk = set()
if know[0]==0:
    print(M)
    for k in range(M):
        party = list(map(int,input().split()))[1:]
else:
    q = deque()
    
    for k in range(M):
        party = list(map(int,input().split()))[1:]
        for i in range(len(party)):
            goParty[party[i]].add(k)
            for j in range(i):
                links[party[i]][party[j]]=1
                links[party[j]][party[i]]=1
    for i in range(1,len(know)):
        check[know[i]]=True
        q.append(know[i])
        noTalk = noTalk|goParty[know[i]]
    while q:
        now = q.popleft()
        for i in range(N+1):
            if check[i]:
                continue
            if links[i][now]==0:
                continue
            check[i]=True
            q.append(i)
            noTalk = noTalk|goParty[i]
    print(M-len(noTalk))