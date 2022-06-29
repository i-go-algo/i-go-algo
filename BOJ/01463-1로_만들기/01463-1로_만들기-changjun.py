# git commit -m "submit : BOJ 01463 1로 만들기 (changjun)"

from collections import deque

n = int(input())

lst = [0]*(n+1)

q = deque()

q.append(n)

while q:
    tmp = q.popleft()
    if tmp%3==0:
        num = tmp//3
        if lst[num] == 0 or lst[num] > lst[tmp] + 1:
            lst[num] = lst[tmp] + 1
            q.append(num)
    if tmp%2==0:
        num = tmp//2
        if lst[num] == 0 or lst[num] > lst[tmp] + 1:
            lst[num] = lst[tmp] + 1
            q.append(num)
    if tmp:
        num = tmp-1
        if lst[num] == 0 or lst[num] > lst[tmp] + 1 and num!=0:
            lst[num] = lst[tmp] + 1
            q.append(num)
print(lst[1])