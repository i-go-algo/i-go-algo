# git commit -m "submit : BOJ 16236 아기 상어 (eonyong)"
import sys
from collections import deque
input = sys.stdin.readline


def BFS(r, c, arr, n, shark, cnt, answer):
    # 중복 방문을 피하기 위한 visited list를 만들어 준다.
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[r][c] = True
    # 현재 상어가 있는 위치와 경로 0을 fishes list에 저장
    fishes = deque([(r, c, 0)])
    flag_box = []
    # 상어가 위치할 수 있는 곳을 계속 헤엄치며 거리를 탐색
    while fishes:
        y, x, v = fishes.popleft()
        # 상하좌우를 누비며 물고기가 있는지 확인
        for j, i in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
            nj, ni = y + j, x + i
            # 자신의 크기 이하인 친구들의 영역을 움직인다
            if 0 <= nj < n and 0 <= ni < n and arr[nj][ni] <= shark and not visited[nj][ni]:
                visited[nj][ni] = True
                # 갈 수 있는 영역을 fishes list에 저장
                fishes.append((nj, ni, v + 1))
                # 만약에 자신보다 덩치가 작은 물고기가 있는 영역이면 flag_box에 저장
                if 0 < arr[nj][ni] < shark:
                    flag_box.append((nj, ni, v + 1))
    else:
        # 다 돌고 나서 flag_box에 물고기가 저장되어 있으면
        if flag_box:
            # 크기, row, col 순으로 작은 순으로 정렬하고 가장 첫번째 요소를 꺼낸다
            flag_box.sort(key=lambda x: (x[-1], x[0], x[1]))
            row, col, dist = flag_box[0]
            # 상어를 이동시키고 원래 있던 자리는 0으로 만들어 준다 
            arr[row][col] = 9
            arr[r][c] = 0
            # 잡아먹은 물고기수 + 1, 배열, 행, 열, 지금까지 걸은 거리 반환
            return cnt + 1, arr, row, col, dist + answer
        else:
            # -1, 배열, 행, 열, 지금까지 걸은 거리 반환
            return -1, arr, r, c, answer


n = int(input())
answer = 0
boards = []
shark = 2
r, c = 0, 0
for row in range(n):
    ls = list(map(int, input().split()))
    for col in range(n):
        if ls[col] == 9:
            r, c = row, col
    boards.append(ls)

cnt = 0
# cnt가 -1이 될 때까지 계속 탐색을 진행
while cnt != -1:
    cnt, boards, r, c, answer = BFS(r, c, boards, n, shark, cnt, answer)
    # 만약 상어의 크기와 잡아먹은 물고기 수가 같으면 상어는 1만큼 성장하고 cnt 리셋
    if shark == cnt:
        cnt = 0
        shark += 1
else:
    # 총 움직인 거리 출력
    print(answer)
