# git commit -m "submit : BOJ 15652 N과 M (4) (eonyong)"
def prune(i, n, arr, ls, m):
    if len(arr) == m:
        print(*arr)
    else:
        for j in range(i, n):
            arr.append(ls[j])
            prune(j, n, arr, ls, m)
            arr.pop()


n, m = map(int, input().split())

prune(0, n, [], range(1, n + 1), m)
