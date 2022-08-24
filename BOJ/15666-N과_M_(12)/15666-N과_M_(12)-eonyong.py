# git commit -m "submit : BOJ 15666 N과 M (12) (eonyong)"
import sys
from itertools import combinations_with_replacement

n, m = map(int, sys.stdin.readline().split())
arr = sorted(map(int, sys.stdin.readline().split()))
for cwp in sorted(set(combinations_with_replacement(arr, m))):
    print(*cwp)