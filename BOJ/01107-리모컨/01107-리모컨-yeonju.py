import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
li = set(input().split())

ans = abs(100 - n)

for num in range(1000000): 
    for i in str(num):
        if i in li:
            break
    else:
        ans = min(ans, len(str(num)) + abs(n - num))

print(ans)
