# git commit -m "submit : BOJ 07662 이중 우선순위 큐 (eonyong)"
import heapq
import sys

for _ in range(int(sys.stdin.readline())):
    minHeap, maxHeap, cnt = [], [], 0
    for _ in range(int(sys.stdin.readline())):
        command, value = sys.stdin.readline().split()
        if command == 'I':
            cnt += 1
            heapq.heappush(minHeap, int(value))
            heapq.heappush(maxHeap, -int(value))
        else:
            if cnt:
                cnt = max(cnt - 1, 0)
                heapq.heappop(minHeap) if value == '-1' else heapq.heappop(maxHeap)
    print('EMPTY') if not cnt else print(-heapq.heappop(maxHeap), heapq.heappop(minHeap))
