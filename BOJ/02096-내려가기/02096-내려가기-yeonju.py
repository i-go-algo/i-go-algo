import sys
input = sys.stdin.readline


def find_max():
    for next_row in range(1, n):
        x, y, z = max_score[0], max_score[1], max_score[2]
        max_score[0] = max(x, y) + arr[next_row][0]
        max_score[1] = max(x, y, z) + arr[next_row][1]
        max_score[2] = max(y, z) + arr[next_row][2]
        x, y, z = max_score[0], max_score[1], max_score[2]


def find_min():
    for next_row in range(1, n):
        x, y, z = min_score[0], min_score[1], min_score[2]
        min_score[0] = min(x, y) + arr[next_row][0]
        min_score[1] = min(x, y, z) + arr[next_row][1]
        min_score[2] = min(y, z) + arr[next_row][2]
        x, y, z = min_score[0], min_score[1], min_score[2]


arr = []
n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    arr.append([a, b, c])

max_score = [arr[0][0], arr[0][1], arr[0][2]]
min_score = [arr[0][0], arr[0][1], arr[0][2]]

find_max()
find_min()
print(max(max_score), min(min_score))
