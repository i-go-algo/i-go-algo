n, m = map(int, input().split())
dic = dict()

for i in range(1, n + 1):
    pokemon = input()
    dic[i] = pokemon
    dic[pokemon] = i

for _ in range(m):
    check = input()
    print(dic[int(check)] if check.isdigit() else dic[check])
