import sys
input = sys.stdin.readline

alphabet = [input().rstrip() for _ in range(2)]
horizontal, vertical = len(alphabet[0]) + 1, len(alphabet[1]) + 1

arr = [[0 for _ in range(horizontal)] for _ in range(vertical)]

for i in range(1, vertical):
    for j in range(1, horizontal):
        if alphabet[1][i - 1] == alphabet[0][j - 1]:
            if i == 1 or j == 1:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i - 1][j - 1] + 1
        else:
            arr[i][j] = max(arr[i - 1][j], arr[i][j - 1])

print(arr[-1][-1])
