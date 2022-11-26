# git commit -m "submit : BOJ 01005 ACM Craft (eonyong)"

import sys
from collections import deque

input = sys.stdin.readline

# 해당 문제는 위상정렬을 이용한 문제이다.
# 위상 문제에 대해서 한번 공부를 해보고 진행하는 것이 좋다고 판단된다.

for _ in range(int(input())):
    n, m = map(int, input().split())
    # 각 노드의 건설 소요시간 리스트
    spend_times = list(map(int, input().split()))
    nodes = [[] for _ in range(n)]
    leaves = [0 for _ in range(n)]
    # 위상 정령이기에 왕복이 아닌 편도 방향 node
    for _ in range(m):
        s, e = map(int, input().split())
        nodes[s - 1].append(e - 1)
        # 도착지점이 가진 가지 수를 추가
        leaves[e - 1] += 1
        
    # 해당 goal을 만드는데 드는 시간
    goal = int(input()) - 1
    
    # 각 건물을 짓기 위해 걸리는 시간을 저장
    times = [0 for _ in range(n)]
    
    # 건설 순서를 저장해서 쭉 만들어나갈 deque
    soonseo = deque()
    
    # leaves를 돌면서 가지수가 없는(출발지점인) 노드를 soonseo에 모두 저장
    # 처음에는 무조건 하나만 있다고 생각하고 진행해서 중간에 틀렸다.
    # 그리고 0인 idx의 times에 건설 시간을 저장
    for idx in range(n):
        if leaves[idx] == 0:
            soonseo.append(idx)
            times[idx] = spend_times[idx]
            
    # 각 건설 순서를 끄집어 내면서 탐색 시작
    while soonseo:
        t = soonseo.popleft()
        # t의 노드를 돌면서 노드를 제거하고 만약에 0이면 soonseo에 그 값을 저장
        # 이후에 가려고하는 노드의 건설 시간 + 현재 위치의 총 건설시간 과 가려고 하는 위치의 총 건설시간을 비교하여
        # 큰 값으로 업데이트
        for value in nodes[t]:
            leaves[value] -= 1
            if leaves[value] == 0:
                soonseo.append(value)
            times[value] = max(times[value], times[t] + spend_times[value])
            
    # goal의 총 건설 시간을 출력
    print(times[goal])
