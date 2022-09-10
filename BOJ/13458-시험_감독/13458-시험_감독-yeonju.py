n = int(input())
a_li = list(map(int, input().split()))
b, c = map(int, input().split())
cnt = 0

for each in a_li:
    each -= b
    cnt += 1
    if each > 0:
        cnt += each // c
        if each % c != 0:
            cnt += 1

print(cnt)
