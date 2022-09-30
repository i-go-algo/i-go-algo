# git commit -m "submit : BOJ 17779 게리맨더링 2 (eonyong)"
import sys
input = sys.stdin.readline
n = int(input())
boards = [list(map(int, input().split())) for _ in range(n)]

total = sum(map(sum, boards))

answer = float('inf')

for row in range(n):
    for col in range(n):
        for d1 in range(1, n):
            for d2 in range(1, n):
                if col + d1 + d2 < n and 0 <= row - d1 < row + d2 - d1 < row + d2 < n:
                    values = [0, 0, 0, 0, 0]
                    
                    for r in range(row):
                        if r < row - d1:
                            for c in range(col + d1 + 1):
                                values[0] += boards[r][c]
                        else:
                            for c in range(col - r + row):
                                values[0] += boards[r][c]

                    for r in range(row + d2 - d1 + 1):
                        if r < row - d1:
                            for c in range(col + d1 + 1, n):
                                values[1] += boards[r][c]
                        else:
                            for c in range(col + 2 * d1 + 1 + r - row, n):
                                values[1] += boards[r][c]

                    for r in range(row, n):
                        if r < row + d2 + 1:
                            for c in range(col + r - row):
                                values[2] += boards[r][c]
                        else:
                            for c in range(col + d2):
                                values[2] += boards[r][c]

                    for r in range(row + d2 - d1 + 1, n):
                        if r <= row + d2:
                            for c in range(col + d2 - r + row + d2 + 1, n):
                                values[3] += boards[r][c]
                        else:
                            for c in range(col + d2, n):
                                values[3] += boards[r][c]
                                
                    values[4] = total - sum(values[:4])
                    max_val, min_val = max(values), min(values)
                    if answer > max_val - min_val:
                        answer = max_val - min_val
print(answer)