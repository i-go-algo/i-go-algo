# git commit -m "submit : BOJ 01107 리모컨 (eonyong)"
import sys
from itertools import product

# 누른 버튼의 갯수를 측정하기 위한 함수
def TenBagger(n) -> int:
    for idx in range(len(n)):
        if n[idx] != '0':
            return len(n) - idx
    return 1


n = list(sys.stdin.readline().strip())
m = int(sys.stdin.readline())
# 고장난 버튼이 있는 경우에는 고장난 숫자를 빼주고, m이 0이면 0 ~ 9까지 숫자를 string 형식으로 저장
buttons = list(set(map(str, range(10))) - set(map(str, sys.stdin.readline().split()))) if m else list(map(str, range(10)))
# 우리가 보고 싶은 채널의 정수형
goal = int(''.join(n))
# 초기 채널번호가 100이므로 goal과 100의 차이를 미리 저장
answer = abs(goal - 100) if goal != 100 else 0

# 만약 9 에서 10으로 넘어가거나, 10에서 9로 넘어가는 경우가 최소일 수도 있어서,,,
for i in [-1, 0, 1]:
    # 채널의 갯수가 1개 이상이므로 0보다 클 때,
    if len(n) + i > 0:
        # itertools의 product를 이용해 중복 사용 가능하게 permutations
        for cwr in product(buttons, repeat=len(n) + i):
            # 구한 값을 정수형으로 변형
            channel = int(''.join(cwr))
            answer = min(abs(channel - goal) + TenBagger(cwr), answer)
print(answer)
