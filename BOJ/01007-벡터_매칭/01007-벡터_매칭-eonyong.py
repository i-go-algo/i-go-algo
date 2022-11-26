# git commit -m "submit : BOJ 01007 벡터 매칭 (eonyong)"
import sys
from itertools import combinations

input = sys.stdin.readline

for _ in range(int(input())):
    tot_x, tot_y = float('inf'), float('inf')
    answer = float('inf')
    n = int(input())
    graphs = [list(map(int, input().split())) for _ in range(n)]
    x, y = map(sum, zip(*graphs))
    for combi in combinations(graphs, n // 2):
        tmp_x, tmp_y = map(sum, zip(*combi))
        answer = min(answer, pow((x - 2 * tmp_x) ** 2 + (y - 2 * tmp_y) ** 2, .5))
    print(answer)
