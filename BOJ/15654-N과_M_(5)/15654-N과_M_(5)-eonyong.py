# git commit -m "submit : BOJ 15654 N과 M (5) (eonyong)"
import sys
from itertools import permutations


def Prunes(i, n, arr, ans):
    if i == n:
        print(ans)
    else:
        for j in range(n):
            ans.append(arr[j])
            Prunes(i + 1, n, arr, ans)
            ans.pop()


n, m = map(int, sys.stdin.readline().split())
arr = sorted(list(map(int, sys.stdin.readline().split())))
for permu in sorted(set(permutations(arr, m))):
    print(*permu)