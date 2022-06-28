# git commit -m "submit : BOJ 01107 리모컨 (yoonseok)"
INF = 10000000000
def check(num,mf):
    if num==0 and num in mf:
        return False
    while num>0:
        temp = num%10
        if temp in mf:
            return False
        num=num//10
    return True
N = int(input())
nums = int(input())

if nums!=0:
    mf = list(map(int,input().split()))
else:
    mf = []
buttons = [INF] *(10000001)
now = 100
for i in range(max(N*2+1,100)):
    if check(i,mf):
        buttons[i] = abs(N-i)+min(len(str(i)),abs(100-i))
    else:
        buttons[i] = abs(N-100)
   
print(min(buttons))