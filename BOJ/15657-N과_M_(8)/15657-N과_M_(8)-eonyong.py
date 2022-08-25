# git commit -m "submit : BOJ 15657 N과 M (8) (eonyong)"
import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for cwp in combinations_with_replacement(arr, m):
    print(*cwp)