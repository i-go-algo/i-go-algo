n, m = map(int, input().split())
never_heard_of = set()
both = set()

for i in range(n):
    never_heard_of.add(input())

for i in range(m):
    temp = input()
    if temp in never_heard_of:
        both.add(temp)

print(len(both))

for i in sorted(list(both)):
    print(i)
