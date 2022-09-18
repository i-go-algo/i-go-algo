from itertools import combinations


def cal(team1):

    global min_difference

    team1 = list(team1)
    for i in people:
        if i not in list(team1):
            team2.append(i)
    # print(team1, team2)
    capability1 = capability2 = 0

    for i in team1:
        for j in team1:
            # print(i,j)
            # print(s[i][j])

            if i != j:
                capability1 += s[i][j]

    for i in team2:
        for j in team2:
            # print(i, j)
            # print(s[i][j])

            if i != j:
                capability2 += s[i][j]

    if abs(capability1-capability2) < min_difference:
        min_difference = abs(capability1-capability2)


n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]
people = [i for i in range(n)]

min_difference = int(1e9)
for c in combinations(people, n//2):
    team1 = []
    team2 = []
    cal(c)

print(min_difference)
