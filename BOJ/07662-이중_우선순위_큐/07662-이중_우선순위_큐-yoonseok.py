# git commit -m "submit : BOJ 07662 이중 우선순위 큐 (yoonseok)"
import heapq

TC = int(input())

for tc in range(TC):
    N = int(input())
    max_q = []
    min_q = []

    removed = [False]*N
    for i in range(N):
        command, value = input().split()
        value = int(value)
        if command=='I':
            heapq.heappush(max_q,(-value,i))
            heapq.heappush(min_q,(value,i))
            removed[i]=True
            
        if command=='D':
            if value==-1:
                while min_q and not removed[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    removed[min_q[0][1]]=False
                    heapq.heappop(min_q)
            else:
                
                while max_q and not removed[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    removed[max_q[0][1]]=False
                    heapq.heappop(max_q)
    if not max_q or not min_q:
        print("EMPTY")
    else:
        max_value = -max_q[0][0]
        min_value = min_q[0][0]
        print(max_value,min_value)
    
    
