# git commit -m "submit : BOJ 01107 리모컨 (eonyong)"

# 백준에 있는 테스트 케이스는 다 통과 하는데 뭐가 걸리는지 모르겠어요 ㅠㅠㅠㅠㅠ
# 내일까지 다시 해보겠습니다..
def remote(i, channel, button, n):
    global answer
    if i == 6:
        ch = len(list(map(str, str(channel))))
        answer = min(abs(channel - n) + ch, answer)
    else:
        for j in button:
            channel = channel * 10 + j
            remote(i + 1, channel, button, n)
            channel //= 10


global answer
n = int(input())
m = int(input())
answer = float('inf')
if m:
    numbers = list(map(int, input().split()))
else:
    numbers = []
buttons = []
for num in range(10):
    if num not in numbers:
        buttons.append(num)

remote(0, 0, buttons, n)
print(min(answer, abs(100 - n)))

