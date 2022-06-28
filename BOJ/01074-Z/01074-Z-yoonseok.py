# git commit -m "submit : BOJ 01074 Z (yoonseok)"
N, r, c = map(int,input().split())
size = 2**(N-1)
loc = []
while (size>=1):
    loc.append((r//size,c//size))
    r = r%size
    c = c%size
    size=size//2
size = (2**(N-1))**2
answer = 0
for l in loc:
    answer+=(l[0]*2+l[1])*size
    size=size//4
print(answer)