# git commit -m "submit : BOJ 01629 곱셈 (yoonseok)"
def power(A, B,C):
    if B==0:
        return 1
    temp = power(A,B//2,C)
    if B%2==0:
        return temp*temp%C
    else:
        return (temp*temp%C)*A%C

A, B, C = map(int,input().split())
print(power(A,B,C))