import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    min_h = []
    max_h = []
    dic = defaultdict(int)

    k = int(input())

    for _ in range(k):
        operation, num = map(str, input().split())

        if operation == 'I':
            heapq.heappush(min_h, int(num))
            heapq.heappush(max_h, -int(num))
            dic[int(num)] += 1

        else:
            if num == '-1':
                while min_h:
                    temp = heapq.heappop(min_h)

                    if dic[temp] > 0:
                        dic[temp] -= 1
                        break

            elif num == '1':
                while max_h:
                    temp = -heapq.heappop(max_h)

                    if dic[temp] > 0:
                        dic[temp] -= 1
                        break

    li = []
    for i in dic:
        if dic[i] > 0:
            li.append(i)

    if li:
        print(max(li), min(li))
    else:
        print('EMPTY')
