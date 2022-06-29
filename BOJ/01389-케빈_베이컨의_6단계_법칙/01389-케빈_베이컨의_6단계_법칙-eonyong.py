# git commit -m "submit : BOJ 01389 케빈 베이컨의 6단계 법칙 (eonyong)"
n, m = map(int, input().split())
users = [[] for _ in range(n + 1)]
distance, member = float('inf'), 0  # 케빈 베이컨 길이, 길이가 가장 짧은 멤버의 번호 저장 변수

for _ in range(m):
    s, e = map(int, input().split())
    users[s].append(e)
    users[e].append(s)

for s in range(1, n + 1):
    visited = [0 for _ in range(n + 1)]  # 멤버별 친구 거리를 저장하는 리스트
    user, cnt = users[s][:], 1  # 시작 멤버의 친구들을 저장하는 리스트와 거리 값 변수
    while user:
        next_visit = []  # 친구의 친구의 친구의,,,저장할 빈 리스트
        for u in user:  # 유져의 친구를 돌면서 친구 거리가 없으면 거리를 입력하고 친구의 친구 탐새
            if not visited[u]:
                visited[u] = cnt
                if users:
                    for end in users[u]:  # 친구의 친구 리스트 돌면서 다음에 방문할 친구를 저장
                        if not visited[end] and s != end:
                            next_visit.append(end)
        user = next_visit[:]  # 친구의 친구를 user에 저장, 거리 1++
        cnt += 1
    # 거리 합을 비교해서 작으면 거리와 멤버 번호를 저장, 같으면 더 작은 멤버 번호로 업데이트
    if distance > sum(visited):
        distance = sum(visited)
        member = s
    elif distance == sum(visited) and member > s:
        member = s
print(member)
