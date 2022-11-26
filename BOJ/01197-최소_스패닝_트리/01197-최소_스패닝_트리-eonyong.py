# git commit -m "submit : BOJ 01197 최소 스패닝 트리 (eonyong)"
import sys
input = sys.stdin.readline

# Kruskal Algorithm을 활용한 문제로 해당 알고리즘을 잘 몰라
# 다른 블로거님을 참고
# https://velog.io/@guri_coding/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EC%8A%A4%ED%84%B0%EB%94%94-%EC%B5%9C%EC%86%8C%EC%8B%A0%EC%9E%A5%ED%8A%B8%EB%A6%ACMST-feat.-Python

# 이동 방향에 따라 parents애 도착 지점을 업데이트
def Union(s, e, parents):
    parents[max(s, e)] = min(s, e)
    return parents


# 만약, 도착지점이 자신과 같다면 그대로 반환, 아니면 계속 탐색하여 마지막 도착지를 반환
def Find(v):
    if v == parents[v]:
        return v
    return Find(parents[v])


answer = 0
n, m = map(int, input().split())

# 모든 간선을 저장하고 노드 간 가중치를 기준으로 오름차순 정렬을 한다.
# 모든 간선을 지나갈 수 있는 최소 거리이기 때문에, 가중치를 기준으로 하는 것이 낫기 때문
nodes = [list(map(int, input().split())) for _ in range(m)]
nodes.sort(key=lambda x: x[2])

# 각 간선의 도착지를 저정할 리스트를 만들어준다.
parents = list(range(n + 1))

# 각 간선 간 관계를 따라 탐색하면서, 가선의 도착지가 겹치지 않으면 다음 단계를 진행.
# parents 업데이트를 완료한 후 해당 가중치 w를 answer에 추가
for s, e, w in nodes:
    if Find(s) != Find(e):
        Union(Find(s), Find(e), parents)
        answer += w

print(answer)
