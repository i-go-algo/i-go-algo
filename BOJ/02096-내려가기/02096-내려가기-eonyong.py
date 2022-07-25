# git commit -m "submit : BOJ 02096 내려가기 (eonyong)"
# 창준님 RGB 코드는 신입니다.,...

def minval(boards):
    r, g, b = boards[0]
    for x, y, z in boards[1:]:
        r, g, b = x + min(g, r), y + min(r, g, b), z + min(b, g)
    return min(r, g, b)


def maxval(boards):
    r, g, b = boards[0]
    for x, y, z in boards[1:]:
        r, g, b = x + max(g, r), y + max(r, g, b), z + max(b, g)
    return max(r, g, b)


n = int(input())

boards = [list(map(int, input().split())) for _ in range(n)]

print(maxval(boards), minval(boards))
