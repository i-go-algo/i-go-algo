n = int(input())
li = []
for i in range(n):
    start, end = map(int, input().split())
    li.append((start, end))

ordered = sorted(li, key=lambda x: (x[1], x[0]))

cnt = 0
end_time = 0

for s, e in ordered:
    if s >= end_time:
        cnt += 1
        end_time = e

print(cnt)
