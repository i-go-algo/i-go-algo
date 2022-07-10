# git commit -m "submit : BOJ 01676 팩토리얼 0의 개수 (yoonseok)"
N = int(input())
def count5(num):
    res = 0
    while not num%5:
        res+=1
        num=num//5
    return res
def count2(num):
    res = 0
    while not num%2:
        res+=1
        num=num//2
    return res
twos = 0
fives = 0
for i in range(1,N+1):
    twos+=count2(i)
    fives+=count5(i)
print(min(twos,fives))