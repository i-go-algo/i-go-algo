# git commit -m "submit : BOJ 02630 색종이 만들기 (changjun)"

n = int(input())

lst = [list(map(int,input().split())) for _ in range(n)]


ans = [0, 0]

def plus(tmp):
    if tmp == 0:
        ans[0] = ans[0] + 1
    elif tmp == 1:
        ans[1] = ans[1] + 1

def func(x, y, m):
    tmp = lst[x][y]
    if m == 1:
        plus(tmp)
        return

    for i in range(m):
        for j in range(m):
            if lst[x + i][y + j] != tmp:
                tmp_m = m//2
                for k in range(2):
                    for l in range(2):
                        func(x + k*tmp_m, y + l * tmp_m, tmp_m)
                return
    plus(tmp)
    return

func(0, 0, n)
for i in range(2):
    print(ans[i])