# git commit -m "submit : BOJ 15684 사다리 조작 (eonyong)"
def ladders(cnt, ladder, n, h, boards, zeros):
    global flag
    if flag == float('inf'):
        # 사다리를 다 놓았으면 game진행, 아니면 사다리 더 놓으러 가기
        if cnt == ladder:
            # 게임이 조건을 만족하고 놓은 갯수가 작으면 flag에 저장
            if game(n, h, boards) and flag > cnt:
                flag = cnt
        else:
            # 놓을 수 있는 사다리 위치를 순회하면서
            for r, c in zeros:
                # 해당 위치에서 길이가 2인 공간이 모두 0인 경우, 사다리를 놓는다.
                if boards[r][c + 1] == boards[r][c] == 0:
                    boards[r][c], boards[r][c + 1] = 1, -1
                    # 사다리 타기 진행
                    ladders(cnt + 1, ladder, n, h, boards, zeros)
                    boards[r][c], boards[r][c + 1] = 0, 0


# 사다리 타기 진행
def game(n, h, boards):
    count = 0 # 같은 위치로 돌아오는 사다리 수 저장
    for col in range(n):
        first = col # 처음 위치 저장
        for row in range(h):
            if boards[row][col] == 1:
                col += 1
            elif boards[row][col] == -1:
                col -= 1
        else:
            # 처음 위치와 같으면 count++
            if col == first:
                count += 1
            else:
                return False
    else:
        # 모두 같은 위치에 도착 했으면 True 반환
        if count == n:
            return True


global flag
n, m, h = map(int, input().split())
boards = [[0] * n for _ in range(h)]
flag = float('inf')
zeros = []

for _ in range(m):
    r, c = map(int, input().split())
    # 1의 경우에는 오른쪽, -1의 경우에는 왼쪽
    boards[r - 1][c - 1] = 1
    boards[r - 1][c] = -1

# 사다리 놓을 수 있는 위치 저장
for row in range(h):
    for col in range(n - 1):
        if boards[row][col] == boards[row][col + 1] == 0:
            zeros.append([row, col])

# 새로 놓는 사다리의 갯수를 0 ~ 3까지 놓는 경우의 수
for idx in range(4):
    ladders(0, idx, n, h, boards, zeros)
else:
    if flag != float('inf'):
        print(flag)
    else:
        print(-1)
