# git commit -m "submit : BOJ 01202 보석 도둑 (yoonseok)"
import heapq

n, k = map(int,input().split())

gem_list = [list(map(int,input().split())) for _ in range(n)]
bag_list = [int(input()) for _ in range(k)]
gem_list.sort()
bag_list.sort()

result = 0
temp = []

for i in bag_list:
    while gem_list and i>=gem_list[0][0]:
        heapq.heappush(temp,-gem_list[0][1])
        heapq.heappop(gem_list)
       
    if temp:
        result += heapq.heappop(temp)
print(-result)