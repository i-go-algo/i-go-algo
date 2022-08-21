# git commit -m "submit : BOJ 15652 N과 M (4) (changjun)"

n, m = map(int,input().split())

lst = range(1, n+1)


def func(ans):
    if len(ans) == m:
        print(*ans)
        return
    for i in lst:
        if ans:
            if ans[-1] <= i:
                ans.append(i)
                func(ans)
                ans.pop()
        else:
            ans.append(i)
            func(ans)
            ans.pop()

        

func([])
