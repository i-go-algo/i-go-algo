# git commit -m "submit : BOJ 01620 나는야 포켓몬 마스터 이다솜 (changjun)"

n, m = map(int,input().split())

dic = dict()
for i in range(n):
    tmp = input()
    dic[str(i+1)] = tmp
    dic[tmp] = i+1
    
for _ in range(m):
    print(dic[input()])