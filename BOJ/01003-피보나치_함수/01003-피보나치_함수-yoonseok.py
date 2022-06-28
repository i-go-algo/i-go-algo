# git commit -m "submit : BOJ 01003 피보나치 함수 (yoonseok)"
T = int(input())
n0 = [1,0]
n1 = [0,1]
for i in range(T):
    N = int(input())
    if len(n0) <= N:
        for i in range(len(n0),N+1):
            n0.append(n0[i-1]+n0[i-2])
            n1.append(n1[i-1]+n1[i-2])
    print(n0[N],n1[N])