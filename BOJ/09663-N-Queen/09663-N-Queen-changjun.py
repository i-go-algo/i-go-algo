# git commit -m "submit : BOJ 09663 N-Queen (changjun)"

n = int(input())

lst = [0] * n

res = 0


def func(index):
    if index == n:
        global res
        res += 1
        return
    # i : 채워넣을 것
    for i in range(n):
        # j : 차있는 것
        for j in range(index):
            if lst[j] == i:
                break
            elif abs(j - index) == abs(i - lst[j]):
                break
        else:
            lst[index] = i
            func(index + 1)
            lst[index] = 0


func(0)
print(res)
