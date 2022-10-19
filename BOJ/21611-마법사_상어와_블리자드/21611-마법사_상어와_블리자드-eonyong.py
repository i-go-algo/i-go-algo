# git commit -m "submit : BOJ 21611 마법사 상어와 블리자드 (eonyong)"
import sys
from collections import deque
input = sys.stdin.readline

# 폭탄 방향
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
# 회전 방향
ro_y, ro_x = [0, 1, 0, -1], [-1, 0, 1, 0]

# 초기 구성 및 마법 시전 순서 저장 리스트
n, m = map(int, input().split())
boards = [list(map(int, input().split())) for _ in range(n)]
magics = deque([list(map(int, input().split())) for _ in range(m)])
answer = 0
# 마법 시전
while magics:
    d, s = magics.popleft()

    # d 방향으로 s 거리만큼 구슬 제거(0으로 만듬)
    row, col = n // 2, n // 2
    for _ in range(s):
        row, col = row + dy[d - 1], col + dx[d - 1]
        boards[row][col] = 0

    # boards를 회전 하며 0이 아닌 값을 snake_num에 저장
    s_y, s_x, rot = n // 2, n // 2, 0
    cnt, pos_cnt = 1, 0
    snake_num = []
    while cnt <= n:
        # cnt만큼의 거리 이동을 2번 진행하면 cnt + 1, 이동 루프 마다 반시계방향으로 방향 회전
        if pos_cnt == 2:
            cnt += 1
            pos_cnt = 0
        for _ in range(cnt):
            s_y, s_x = s_y + ro_y[rot], s_x + ro_x[rot]
            if 0 <= s_y < n and 0 <= s_x < n and boards[s_y][s_x]:
                snake_num.append(boards[s_y][s_x])
        else:
            rot = (rot + 1) % 4
            pos_cnt += 1

    # 저장된 값들 모아서 값은 수가 4번 이상 되는 것들을 제거하기 위한 while
    while True:
        after_boom, boom_temp = [], []
        for num in snake_num:
            # 비어있으면 boom_temp에 추가
            if not boom_temp:
                boom_temp.append(num)
            else:
                # boom_temp와 num이 다르면 after_boom에 추가하는데
                # 4 미만인 경우는 추가, 길이가 4이상 파괴 후 answer에 길이 * 파괴 구슬의 번호를 더해줌 
                if boom_temp[-1] != num:
                    if len(boom_temp) < 4:
                        after_boom.extend(boom_temp)
                    else:
                        answer += boom_temp[-1] * len(boom_temp)
                    boom_temp = [num]
                else:
                    boom_temp.append(num)
        else:
            if len(boom_temp) < 4:
                after_boom.extend(boom_temp)
            else:
                answer += boom_temp[-1] * len(boom_temp)
                
        # 변화가 없으면 while문 탈출, 아니면 snake_num 업데이트
        if snake_num == after_boom:
            break
        else:
            snake_num = after_boom[:]
    
    # 각 구슬의 갯수와 번호를 구해주는 리스트 구형
    snake_group, group_temp = [], []
    for num in snake_num:
        if not group_temp:
            group_temp.append(num)
        else:
            # num과 리스트에 저장된 값이 다르면 길이와 그 값을 snake_group에 추가
            if num != group_temp[-1]:
                snake_group.extend([len(group_temp), group_temp.pop()])
                group_temp = [num]
            else:
                group_temp.append(num)
    else:
        if group_temp:
            snake_group.extend([len(group_temp), group_temp.pop()])

    # 새로 업데이트된 snake를 boards에 구성
    boards = [[0 for _ in range(n)] for _ in range(n)]
    s_y, s_x, rot = n // 2, n // 2, 0
    cnt, pos_cnt = 1, 0
    snake_num = deque(snake_group)
    flag = True
    while cnt <= n and flag:
        if pos_cnt == 2:
            cnt += 1
            pos_cnt = 0
        for _ in range(cnt):
            s_y, s_x = s_y + ro_y[rot], s_x + ro_x[rot]
            if not snake_num:
                flag = False
                break
            if 0 <= s_y < n and 0 <= s_x < n:
                boards[s_y][s_x] = snake_num.popleft()
        else:
            rot = (rot + 1) % 4
            pos_cnt += 1
print(answer)