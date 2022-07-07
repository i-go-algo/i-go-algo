# git commit -m "submit : BOJ 01697 숨바꼭질 (eonyong)"
n, m = map(int, input().split())
if n == m:
    print(0)
else:
    cnt = 0
    max_val = max(n, m) * 2 + 1  # n > m 인 경우를 생각 했어야 하는 문제 였음
    visited = [False for _ in range(max_val)]
    visited[n], histories = True, [n]
    while histories:
        cnt, next_history = cnt + 1, []
        for history in histories:
            for num in [history + 1, history - 1, history * 2]:
                if 0 <= num < max_val and not visited[num]:
                    visited[num] = True
                    next_history.append(num)
        histories = next_history[:] if not visited[m] else []
    print(cnt)