# git commit -m "submit : BOJ 13458 시험 감독 (eonyong)"
import sys

answer = 0
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B, C = map(int, sys.stdin.readline().split())

for student in A:
    answer += 1
    student -= B
    if student > 0:
        if student % C:
            answer += student // C + 1
        else:
            answer += student // C
print(answer)