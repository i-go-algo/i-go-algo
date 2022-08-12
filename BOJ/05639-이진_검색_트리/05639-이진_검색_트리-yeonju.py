import sys
sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline


def dfs(start, end):
    # 종료 조건 안 와닿아ㅏㅏㅏㅏ 예시가 뭔데~~
    if start > end:
        return

    temp = end + 1

    # 서브 트리 찾기
    for i in range(start + 1, end + 1):
        if graph[start] < graph[i]:
            temp = i
            break

    dfs(start + 1, temp - 1)    # 왼쪽 서브 트리 재귀적으로 탐색
    dfs(temp, end)  # 오른쪽 서브 트리 재귀적으로 탐색

    print(graph[start])


graph = []

while True:
    try:
        graph.append(int(input()))
    except:
        break

dfs(0, len(graph) - 1)
