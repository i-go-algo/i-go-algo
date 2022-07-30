import sys
input= sys.stdin.readline

n, m = map(int, input().split())

numerator = 1
denominator = 1

for i in range(n, n - m, -1):
    numerator *= i
for i in range(1, m + 1):
    denominator *= i

print(numerator // denominator)
