# git commit -m "submit : BOJ 02606 바이러스 (eonyong)"
n = int(input())
nodes = int(input())
arr = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(nodes):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

viruses = arr[1]
visited[1] = True
cnt = 0
while viruses:
    computers = []
    for virus in viruses:
        if not visited[virus]:
            visited[virus] = True
            cnt += 1
            computers += arr[virus]
    viruses = computers[:]
print(cnt)