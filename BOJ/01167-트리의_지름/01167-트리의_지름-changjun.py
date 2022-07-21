# git commit -m "submit : BOJ 01167 트리의 지름 (changjun)"




from collections import defaultdict, deque

v = int(input())

dic = defaultdict(dict)

for _ in range(v):
    node, *lst, end = map(int,input().split())
    for i in range(len(lst)//2):
        dic[node][lst[2*i]] = lst[2*i+1]


ans = 0
for node in range(1, v+1):
    visited = set()
    visited.add(node)
    q = deque()
    q.append(node)
    tmp_ans = 0
    while q:
        tmp = q.popleft()
        tmp_node = -1
        tmp_len = 0
        for next_node in dic[tmp]:
            if next_node not in visited and dic[tmp][next_node] > tmp_len:
                tmp_node = next_node 
                tmp_len = dic[tmp][next_node]
        if tmp_len:
            q.append(tmp_node)
            visited.add(tmp_node)
            tmp_ans += tmp_len
    ans = max(ans, tmp_ans)
print(ans)







# ans = 0
# for node in range(1, v+1):
#     q = deque()
#     for next_node in dic[node]:
#         q.append((dic[node][next_node], {node, next_node}, next_node))

#     while q:
#         cost, node_set, node = q.popleft()
#         for next_node in dic[node]:
#             if next_node not in node_set:
#                 tmp_set = node_set.copy()
#                 tmp_set.add(next_node)
#                 q.append((cost + dic[node][next_node], tmp_set, next_node))
#                 ans = max(ans, cost + dic[node][next_node])

# print(ans)

# ans = 0

# def func(x, distance, visited):
#     global ans
#     ans = max(ans, distance)
#     for node in dic[x]:
#         if node not in visited:
#             visited.add(node)
#             func(node, distance + dic[x][node], visited)
#             visited.remove(node)

# func(1, 0, set())
# print(ans)











# from collections import defaultdict

# v = int(input())

# dic = defaultdict(dict)

# for _ in range(v):
#     node, *lst, end = map(int,input().split())
#     for i in range(len(lst)//2):
#         dic[node][lst[2*i]] = lst[2*i+1]


# ans = 0

# def func(x, distance, visited):
#     global ans
#     ans = max(ans, distance)
#     for node in dic[x]:
#         if node not in visited:
#             visited.add(node)
#             func(node, distance + dic[x][node], visited)
#             visited.remove(node)

# func(1, 0, set())
# print(ans)