# git commit -m "submit : BOJ 14501 퇴사 (eonyong)"
def f(i, n, arr):
    global answer
    if i >= n:
        ans = 0
        for idx in range(n):
            if arr[idx] == 1:
                ans += P[idx]
        else:
            if answer < ans:
                answer = ans
    else:
        for j in range(i, n):
            if not arr[j] and j + T[j] <= n:
                arr[j] = 1
            f(j + T[j], n, arr)
            arr[j] = 0


global answer
N = int(input())
T, P, answer = [], [], 0
for _ in range(N):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

f(0, N, [0] * N)

print(answer)
