# git commit -m "submit : BOJ 01562 계단 수 (eonyong)"
import sys

input = sys.stdin.readline

MOD = 1000000000
answer = 0
n = int(input())
boards = [[[0 for _ in range(1024)] for _ in range(10)] for _ in range(n + 1)]
for idx in range(1, 10):
    boards[1][idx][1 << idx] = 1

for row in range(n):
    for col in range(10):
        for bit in range(1024):
            if col < 9:
                next_bit = bit | (1 << (col + 1))
                boards[row + 1][col + 1][next_bit] = (boards[row + 1][col + 1][next_bit] + boards[row][col][bit]) % MOD
            if col > 0:
                next_bit = bit | (1 << (col - 1))
                boards[row + 1][col - 1][next_bit] = (boards[row + 1][col - 1][next_bit] + boards[row][col][bit]) % MOD

for last in range(10):
    answer = (answer + boards[n][last][-1]) % MOD
print(answer)