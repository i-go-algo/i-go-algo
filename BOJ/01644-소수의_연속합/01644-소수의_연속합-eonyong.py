# git commit -m "submit : BOJ 01644 소수의 연속합 (eonyong)"
import sys

input = sys.stdin.readline

n = int(input())
answer = 0
primes = []
# n이 2이상일 경우, 2보다 작은 소수의 값을 모두 구해서 저장 해줍니다.
if n > 1:
    for i in range(2, n + 1):
        for j in range(2, int(pow(i, .5)) + 1):
            if not i % j:
                break
        else:
            primes.append(i)

# 저장된 소수의 길이를 저장하고
m = len(primes)
# 천천히 돌면서 입력 받은 n보다 크면 break, 같으면 answer + 1 해주고 break
for idx in range(m):
    val = 0
    for s in range(idx, m):
        val += primes[s]
        if val > n:
            break
        elif val == n:
            answer += 1
            break
print(answer)
