# git commit -m "submit : BOJ 11725 트리의 부모 찾기 (yoonseok)"
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
ans = [0]*(N+1)
visit = [False]*(N+1)
con = list([] for i in range(N+1))
for i in range(N-1):
    n1, n2 = map(int,input().split())
    con[n1].append(n2)
    con[n2].append(n1)
visit[1]=True
def make_ans(now):
    for i in con[now]:
        if not visit[i]:
            visit[i]=True
            ans[i]=now
            make_ans(i)
make_ans(1)
for i in range(2,N+1):
    print(ans[i])