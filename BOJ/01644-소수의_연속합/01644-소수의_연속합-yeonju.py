n = int(input())

prime_or_not = [False, False] + [True for i in range(n - 1)]
arr = []

for i in range(2, int(n ** 0.5) + 1):
    if prime_or_not[i]:
        prime_or_not[i * 2 :: i] = [False] * ((n - i) // i)

for i in range(n + 1):
    if prime_or_not[i] is True:
        arr.append(i)

i, j = 0, 0
total = 0
cnt = 0

while True:
    if total == n:
        cnt += 1

    if total > n:
        total -= arr[i]
        i += 1
    elif j == len(arr):
        break
    else:
        total += arr[j]
        j += 1

print(cnt)
