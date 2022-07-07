# git commit -m "submit : BOJ 01764 듣보잡 (eonyong)"
n, m = map(int, input().split())
cards = set()
answer, num = [], 0
for _ in range(n):
    cards.add(input())
for _ in range(m):
    value = input()
    if value in cards:
        answer.append(value)
        num += 1
answer.sort()
print(num)
for idx in range(num):
    print(answer[idx])