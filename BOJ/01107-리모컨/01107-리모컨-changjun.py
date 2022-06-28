# git commit -m "submit : BOJ 01107 리모컨 (changjun)"


n = list(map(int,input()))
num = int(''.join(map(str,n)))
m = int(input())
res = num+100

if 0<m<10:

    broken = set(map(int,input().split()))

    num_set = set(range(10))

    num_set = num_set - broken
    min_num = min(num_set)
    max_num = max(num_set)

    ans = []
    flag = 0

    for i in n:
        if not flag:
            if i in num_set:
                ans.append(i)
            else:
                tmp = 1
                ans_s = False
                ans_b = False
                while i+tmp < 10:
                    if i+tmp in num_set:
                        flag = 'small'
                        ans_s = ans[:]
                        ans_s.append(i+tmp)
                        break
                    tmp += 1 
                tmp = 1
                while i-tmp >= 0:
                    if i-tmp in num_set:
                        ans_b = ans[:]
                        ans_b.append(i-tmp)
                        flag = 'big'
                        break
                    tmp += 1 

        else:
            if ans_b:
                ans_b.append(max_num)
            if ans_s:
                ans_s.append(min_num)


    if ans_s:
        ans_s = int(''.join(map(str,ans_s)))
        click = len(str(ans_s))
        res = min(res, click + abs(num-ans_s))
    if ans_b:
        ans_b = int(''.join(map(str,ans_b)))
        click = len(str(ans_b))
        res = click + abs(ans_b - num)

    if num<200:
        res = min(res, abs(num - 100))
    
    if 1 in num_set:
        tmp_num = int(''.join(map(str,[1] + [min_num]*click)))
        res = min(res, tmp_num - num + click + 1)


if num<100:
    res = min(res, 100-num)
else:
    res = min(res, num-100)
if m==10:
    input()
if m==0:
    res = min(res, len(n))


print(res)