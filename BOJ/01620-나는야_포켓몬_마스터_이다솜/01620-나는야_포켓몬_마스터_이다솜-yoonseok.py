# git commit -m "submit : BOJ 01620 나는야 포켓몬 마스터 이다솜 (yoonseok)"
N, M = map(int,input().split())
pocktonum = dict()
numtopock = ['']*(N+1)
for i in range(N):
    temp = input()
    pocktonum[temp]=i+1
    numtopock[i+1]=temp
for j in range(M):
    question = input()
    if '0'<=question[0]<='9':
        print(numtopock[int(question)])
    else:
        print(pocktonum[question])