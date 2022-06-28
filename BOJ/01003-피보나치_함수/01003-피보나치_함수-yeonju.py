t = int(input())

for tc in range(t):
    n = int(input())
    fibo = [0] * n
    fibo = [(1, 0), (0, 1)] + [0] * (n - 1)

    for i in range(2, n + 1):
        fibo[i] = (fibo[i - 1][0] + fibo[i - 2][0], fibo[i - 1][1] + fibo[i - 2][1])

    print(fibo[n][0], fibo[n][1])
