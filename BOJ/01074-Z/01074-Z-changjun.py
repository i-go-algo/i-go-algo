# git commit -m "submit : BOJ 01074 Z (changjun)"

n, r, c = map(int,input().split())

r += 1
c += 1
n = 2**n
ans = 0
while n:
    n = n//2
    if r <= n:
        if c <= n:
            # 좌상
            pass
        else:
            # 우상
            ans += n**2
            c -= n
    else:
        if c <= n:
            # 좌하
            ans += 2*n**2
            r -= n
        else:
            # 우하
            ans += 3*n**2
            r -= n
            c -= n
print(ans)            
