# git commit -m "submit : BOJ 01676 팩토리얼 0의 개수 (eonyong)"
from math import factorial

n = list(map(int, str(factorial(int(input())))))
m = len(n)
for idx in range(m - 1, -1, -1):
    if n[idx]:
        print(m - idx - 1)
        break
