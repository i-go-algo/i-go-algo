# git commit -m "submit : BOJ 01764 듣보잡 (yoonseok)"
N, M = map(int,input().split())
checking = set()
answer = []
for i in range(N):
    checking.add(input())
for j in range(M):
    nana = input()
    if nana in checking:
        answer.append(nana)
print(len(answer))
answer.sort()
for i in answer:
    print(i)