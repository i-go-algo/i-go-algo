# git commit -m "submit : BOJ 12851 숨바꼭질 2 (changjun)"

from collections import deque

n, k = map(int,input().split())
max_num = int(max(n,k)*2)
q = deque()
q.append((n, 0))

match = 0
cnt = 0
arrive_time = -1
lst = [100000]*(max_num)

if n==k:
    print(0)
    print(1)
else:
    while q:
        position, time = q.popleft()
        for next in [position-1, position+1, 2*position]:
            if next == k:
                if arrive_time == time:
                    cnt+=1
                elif arrive_time == -1:
                    arrive_time = time
                    match = 1
                    cnt += 1
            if 0<=next<max_num and lst[next] > time:
                lst[next] = time + 1
                q.append((next, time+1))

        if match:
            if time != arrive_time:
                break
    print(time)
    print(cnt)


        




