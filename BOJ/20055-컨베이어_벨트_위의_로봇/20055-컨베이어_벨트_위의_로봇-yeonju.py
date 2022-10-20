import sys
input = sys.stdin.readline

n, k = map(int, input().split())
belt = list(map(int, input().split()))
robot = [0 for _ in range(n)]
total = 0
cnt = 0

while total < k:
    # 벨트가 로봇과 함께 한 칸 회전
    # print('1 before belt rotation', belt)
    temp = belt[2 * n - 1]
    for i in range(2 * n - 2, -1, -1):
        belt[i + 1] = belt[i]

    belt[0] = temp

    for i in range(n - 2, -1, -1):
        robot[i + 1] = robot[i]
        robot[i] = 0

    robot[n - 1] = 0

    # print('1 after belt rotation', belt)
    # print()

    # 먼저 올라간 로봇부터 회전하는 방향으로 이동할 수 있으면 이동
    # 없다면 가만히
    # 조건: 이동하려는 칸에 로봇 없음, 해당 칸의 내구도가 1이상

    # print('2 before robot move', robot)
    # print('2 before belt move', belt)
    # print()
    for i in range(n - 2, -1, -1):
        if robot[i] and not robot[i + 1] and belt[i + 1] >= 1:
            robot[i + 1] = robot[i]
            robot[i] = 0
            belt[i + 1] -= 1
            if belt[i + 1] == 0:
                total += 1

    robot[n - 1] = 0

    # print('2 after robot move', robot)
    # print('2 after belt move', belt)
    # 올리는 위치에 있는 칸의 내구도가 0이 아니면 로봇 올림

    # print()
    # print('3 before belt', belt)
    # print('3 robot', robot)
    if belt[0]:
        robot[0] = 1
        belt[0] -= 1
        if belt[0] == 0:
            total += 1

    # print('3 after belt', belt)
    # print('3 robot', robot)
    # print()
    # 내구도가 0인 칸의 개수가 K 개 이상이면 종료

    cnt += 1
    # print('4', total)
    # print('===============================')

print(cnt)
