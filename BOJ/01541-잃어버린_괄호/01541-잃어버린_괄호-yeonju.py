import sys
input = sys.stdin.readline

expression = input().split('-')
res = 0

for i in expression[0].split('+'):
    res += int(i)

for i in expression[1:]:
    for j in i.split('+'):
        res -= int(j)

print(res)
