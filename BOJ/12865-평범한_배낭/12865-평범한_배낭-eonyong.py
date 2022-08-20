# git commit -m "submit : BOJ 12865 평범한 배낭 (eonyong)"
w, h = map(int, input().split())
bags = [[0 for _ in range(h + 1)] for _ in range(w + 1)]
items = [list(map(int, input().split())) for _ in range(w)]

for row in range(1, w + 1):
    for col in range(1, h + 1):
        weight, value = items[row - 1]
        if col < weight:
            bags[row][col] = bags[row - 1][col]
        else:
            bags[row][col] = max(value + bags[row - 1][col - weight], bags[row - 1][col])

print(bags[-1][-1])