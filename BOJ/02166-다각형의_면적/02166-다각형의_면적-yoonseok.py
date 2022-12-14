# git commit -m "submit : BOJ 02166 다각형의 면적 (yoonseok)"
n = int(input())
x, y = [], []
answer = 0
for _ in range(n):
    a, b = map(int,input().split())
    x.append(a)
    y.append(b)
x, y = x + [x[0]], y + [y[0]]

for i in range(n):
    answer += (x[i]*y[i+1])-(x[i+1]*y[i])
print(round(abs(answer)/2,1))