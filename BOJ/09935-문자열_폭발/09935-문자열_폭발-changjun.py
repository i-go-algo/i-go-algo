# git commit -m "submit : BOJ 09935 문자열 폭발 (changjun)"

tmp = input()
bang = list(input())

n = len(bang)
ans = []
for i in tmp:
    ans.append(i)
    if i == bang[-1]:
        if len(ans) >= n and ans[-n:] == bang:
            for _ in range(n):
                ans.pop()
if ans:
    print(''.join(ans))
else:
    print('FRULA')


# while 1:
#     index = tmp.find(bang)
#     if index == -1:
#         break
#     tmp = tmp[:index] + tmp[index + n :]
# if tmp:
#     print(tmp)
# else:
#     print('FRULA')
