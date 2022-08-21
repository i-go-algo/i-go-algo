# git commit -m "submit : BOJ 15666 N과 M (12) (changjun)"

from itertools import permutations

n, m = map(int,input().split())


lst = list(map(int,input().split()))
lst = sorted(lst)
ans_lst = []
def func(ans):
    if len(ans) == m:
        ans_lst.append(tuple(ans))
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

for nums in sorted(list(set(ans_lst))):
    print(*nums)