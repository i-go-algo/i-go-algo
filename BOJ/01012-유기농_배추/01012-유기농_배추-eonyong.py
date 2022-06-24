# git commit -m "submit : BOJ 01012 유기농 배추 (eonyong)"
from collections import deque

for _ in range(int(input())):
    # 가로, 세로, 배추 개수 입력
    m, n, k = map(int, input().split())
    # 텃밭, 텃밭 방문 여부 확인
    boards = [[0] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    # k번 동안, (x, y) 위치에 배추 심기
    for _ in range(k):
        x, y = map(int, input().split())
        boards[y][x] = 1

    # 밭에 풀어놓을 지렁이 마릿 수 넣는 변수
    cnt = 0

    # 텃밭을 돌면서 배추 군집을 세어 본다.
    for row in range(n):
        for col in range(m):
            if boards[row][col] and not visited[row][col]: # 배추가 있고 방문하지 않은 위치이면 지렁이를 추가하고 방문 표시
                cnt += 1
                visited[row][col] = True
                cabbage = deque([[row, col]]) # 배추 위치를 담는 배추 박스
                while cabbage: # 배추가 다 떨어질 때까지
                    r, c = cabbage.popleft()
                    for j, i in [[1, 0], [0, -1], [-1, 0], [0, 1]]: # 상, 하, 좌, 우를 둘러보며 배추가 있는지 확인
                        nj, ni = r + j, c + i
                        if 0 <= nj < n and 0 <= ni < m and boards[nj][ni] and not visited[nj][ni]: # 있으면 방문 표시하고 박스에 배추 위치를 집어 넣는다. 
                            visited[nj][ni] = True
                            cabbage.append([nj, ni])
    print(cnt)