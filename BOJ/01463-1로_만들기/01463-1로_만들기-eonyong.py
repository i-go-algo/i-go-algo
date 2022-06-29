# git commit -m "submit : BOJ 01463 1로 만들기 (eonyong)"
def makeOne(n, cnt):
    global answer
    if n == 1: # n이 1이 되면 answer와 cnt 중 작은 값을 저장
        answer = min(cnt, answer)
    elif n > 1 and answer > cnt: # recursion이랑 TLE 막기 위해 1보다 크고 answer 값보다 작은 경우만 돌게 함
        if not n % 3:
            makeOne(n // 3, cnt + 1)
        if not n % 2:
            makeOne(n // 2, cnt + 1)
        makeOne(n - 1, cnt + 1)


global answer
answer = float('inf') # 최소 횟수를 저장할 변수
n = int(input())
makeOne(n, 0)
print(answer)
