n = int(input())
count_two = 0
count_five = 0

for i in range(n, 0, -1):
    while i % 2 == 0:
        i //= 2
        count_two += 1

    while i % 5 == 0:
        i //= 5
        count_five += 1

print(min(count_two, count_five))
