# git commit -m "submit : BOJ 15657 N과 M (8) (changjun)"

n, m = map(int,input().split())

lst = list(map(int,input().split()))
lst = sorted(lst)

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
