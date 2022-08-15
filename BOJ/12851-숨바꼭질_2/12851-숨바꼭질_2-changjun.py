# git commit -m "submit : BOJ 12851 숨바꼭질 2 (changjun)"

from collections import deque

n, k = map(int,input().split())
max_num = int(max(n,k)*1.5)
q = deque()
q.append((n, 0))

match = 0
cnt = 0

lst = [100000]*(max_num)

while q:
    position, time = q.popleft()
    for next in [position-1, position+1, 2*position]:
        if next == k:
            match = 1
            cnt += 1
            arrive_time = time
        if 0<=next<max_num and lst[next] > time:
            lst[next] = time + 1
            q.append((next, time+1))

    if match:
        if time != arrive_time:
            break
print(time)
print(cnt)


    




