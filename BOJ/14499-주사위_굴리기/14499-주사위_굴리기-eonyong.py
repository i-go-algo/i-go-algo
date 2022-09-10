# git commit -m "submit : BOJ 14499 주사위 굴리기 (eonyong)"
def diceHandle(value, dice, task):
    if task == 1:  # 동쪽
        dice[1][0], dice[1][1], dice[0][3], dice[0][1] = dice[0][1], dice[0][3], dice[1][0], dice[1][1]
    elif task == 2:  # 서쪽
        dice[1][1], dice[1][0], dice[0][1], dice[0][3] = dice[0][1], dice[0][3], dice[1][0], dice[1][1]
    elif task == 3:  # 북쪽
        dice[0] = dice[0][1:] + [dice[0][0]]
    elif task == 4:  # 남쪽
        dice[0] = [dice[0][3]] + dice[0][:-1]
    # 새로운 주사위와 맨 위 숫자 반환
    return dice, dice[0][1]


n, m, y, x, k = map(int, input().split())
# 그림판
boards = [list(map(int, input().split())) for _ in range(n)]
# 방향 수행 리스트
tasks = list(map(int, input().split()))
# task에 따른 방향 dictionary
directions = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}
# dice 앞은 [뒤, 위, 앞, 아래], [좌, 우] 형태
dice = [[0, 0, 0, 0], [0, 0]]
# 맨 위의 숫자 저장할 변수
top = 0

for task in tasks:
    nj, ni = y + directions[task][0], x + directions[task][1]
    if 0 <= nj < n and 0 <= ni < m:
        y, x = nj, ni
        dice, top = diceHandle(boards[y][x], dice, task)
        #   이동한 칸에 쓰여 있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사
        if not boards[y][x]:
            boards[y][x] = dice[0][3]
        #   0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되며, 칸에 쓰여 있는 수는 0이 된다.
        else:
            dice[0][3] = boards[y][x]
            boards[y][x] = 0
        print(top)
