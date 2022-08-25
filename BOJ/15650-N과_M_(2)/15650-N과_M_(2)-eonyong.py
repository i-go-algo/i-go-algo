# git commit -m "submit : BOJ 15650 N과 M (2) (eonyong)"
import sys
from itertools import combinations

n, m = map(int, sys.stdin.readline().split())

for num in combinations(range(1, n + 1), m):
    print(*num)