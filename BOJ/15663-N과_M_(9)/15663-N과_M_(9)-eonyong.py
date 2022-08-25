# git commit -m "submit : BOJ 15663 N과 M (9) (eonyong)"
import sys
from itertools import permutations

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
for cwp in sorted(set(permutations(arr, m))):
    print(*cwp)