# git commit -m "submit : BOJ 01629 곱셈 (changjun)"

a, b, c = map(int,input().split())

a = a % c


def func(x, y):
    if y == 1:
        return x

    if y%2:
        val1 = func(x, y//2)
        val2 = func(x, y//2 + 1)
        return (val1 * val2) % c
    else:
        val = func(x, y//2)
        return (val * val) % c




print(func(a, b))