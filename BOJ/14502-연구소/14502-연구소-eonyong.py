# git commit -m "submit : BOJ 14502 연구소 (eonyong)"
from itertools import combinations
import copy


def bfs(r, c):
    global reverse_cnt, reverse
    if reverse > reverse_cnt:
        for i, j in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nj, ni = r + j, c + i
            if 0 <= ni < W and 0 <= nj < H and not arr_copy[nj][ni]:
                arr_copy[nj][ni] = 2
                reverse_cnt += 1
                bfs(nj, ni)


H, W = map(int, input().split())
arr = [[0] * W for _ in range(H)]
cnt = -3
walls, viruses = [], []
reverse = H * W

for h in range(H):
    ls = list(map(int, input().split()))
    for w in range(W):
        arr[h][w] = ls[w]
        if not ls[w]:
            cnt += 1
            walls.append([h, w])
        elif ls[w] == 2:
            viruses.append([h, w])

for wall in combinations(walls, 3):
    arr_copy = copy.deepcopy(arr)
    for wr, wc in wall:
        arr_copy[wr][wc] = 1

    reverse_cnt = 0
    for virus_y, virus_x in viruses:
        bfs(virus_y, virus_x)
    if reverse > reverse_cnt:
        reverse = reverse_cnt

print(cnt - reverse)