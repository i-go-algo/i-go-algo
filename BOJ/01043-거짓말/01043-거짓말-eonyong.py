# git commit -m "submit : BOJ 01043 거짓말 (eonyong)"
from collections import defaultdict, deque

n, m = map(int, input().split())
truths = deque(list(map(int, input().split()))[1:])
parties = [False] * m
players = defaultdict(set)
rooms = defaultdict(set)
for idx in range(m):
    for member in list(map(int, input().split()))[1:]:
        players[member].add(idx)
        rooms[idx].add(member)

while truths:
    start = truths.popleft()
    for room in players[start]:
        if not parties[room]:
            parties[room] = True
            truths += list(rooms[room])
print(parties.count(False))
