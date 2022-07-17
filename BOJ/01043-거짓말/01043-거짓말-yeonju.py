n, m = map(int, input().split())
truth = set(input().split()[1:])
cnt = 0
parties = []
for _ in range(m):
    parties.append(set(input().split()[1:]))

# 최악의 경우 역순으로 1번 씩 갱신되기 때문에 m 번 순회해야 함
for _ in range(m):
    for party in parties:
        if party & truth:
            truth = truth.union(party)

for party in parties:
    if not party & truth:
        cnt += 1

print(cnt)
