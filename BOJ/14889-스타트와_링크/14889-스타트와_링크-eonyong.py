# git commit -m "submit : BOJ 14889 스타트와 링크 (eonyong)"
def combi(i, n, m, a_team, players, visited, boards):
    global answer
    if i == m:
        b_team = []
        for idx in range(n):
            if not visited[idx]:
                b_team.append(players[idx])
        val = 0
        
        for s in range(m - 1):
            for e in range(s + 1, m):
                a_1, a_2, b_1, b_2 = a_team[s], a_team[e], b_team[s], b_team[e]
                a_score, b_score = boards[a_1][a_2] + boards[a_2][a_1], boards[b_1][b_2] + boards[b_2][b_1]
                val += (a_score - b_score)
        
        if answer > abs(val):
            answer = abs(val)
    else:
        for j in range(n):
            if not visited[j] and a_team[0] < m and (not i or (i and a_team[i - 1] < players[j])):
                a_team[i], visited[j] = players[j], True
                combi(i + 1, n, m, a_team, players, visited, boards)
                a_team[i], visited[j] = 0, False


import sys

global answer
answer = float('inf')
N = int(sys.stdin.readline())
half = N // 2
boards = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
total = sum(map(sum, boards))
players = list(range(N))
combi(0, N, half, [0] * half, players, [False] * N, boards)

print(answer)
