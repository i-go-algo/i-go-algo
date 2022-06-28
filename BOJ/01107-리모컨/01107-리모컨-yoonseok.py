# git commit -m "submit : BOJ 01107 리모컨 (yoonseok)"
INF = 10000000000
def check(num,mf):
    while num>0:
        temp = num%10
        if temp in mf:
            return False
        num=num//10
    return True
N = int(input())
nums = int(input())
mf = []
if nums!=0:
    mf = list(map(int,input().split()))
buttons = [INF] * N*2
now = 100
for i in range(N*2):
    if check(i,mf):
        buttons[i] = abs(N-i)+min(len(str(i)),abs(100-i))
    else:
        buttons[i] = abs(N-100)
print(min(buttons))

