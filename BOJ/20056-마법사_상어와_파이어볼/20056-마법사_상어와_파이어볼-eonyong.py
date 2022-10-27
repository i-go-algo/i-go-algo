# git commit -m "submit : BOJ 20056 마법사 상어와 파이어볼 (eonyong)"
import sys
from collections import defaultdict


def all_odd_or_even(dirs):
    odd_flag, even_flag = False, False
    for d in dirs:
        if d % 2 == 1:
            odd_flag = True
        if d % 2 == 0:
            even_flag = True

    if odd_flag and even_flag:
        return False
    return True


input = sys.stdin.readline

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

answer = 0
n, m, k = map(int, input().split())
fireballs = defaultdict(list)

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    fireballs[(r - 1, c - 1)].append([m, s, d])

for _ in range(k):
    new_fireballs = defaultdict(list)
    for loc, info_list in fireballs.items():
        sy, sx = loc
        for m, s, d in info_list:
            ny = (sy + dr[d] * s) % n
            nx = (sx + dc[d] * s) % n
            new_fireballs[(ny, nx)].append((m, s, d))

    fireballs = new_fireballs.copy()

    new_fireballs = defaultdict(list)
    for loc, info_list in fireballs.items():
        if len(info_list) == 1:
            new_fireballs[loc].append(info_list[0])
            continue

        sum_m, sum_s, dirs = 0, 0, []
        for m, s, d in info_list:
            sum_m += m
            sum_s += s
            dirs.append(d)
        new_m = int(sum_m / 5)
        if new_m == 0:
            continue
        new_s = int(sum_s / len(info_list))
        new_dirs = [0, 2, 4, 6] if all_odd_or_even(dirs) else [1, 3, 5, 7]
        for new_d in new_dirs:
            new_fireballs[loc].append((new_m, new_s, new_d))

    fireballs = new_fireballs.copy()

result = 0
for loc, info_list in fireballs.items():
    for m, s, d in info_list:
        result += m
print(result)