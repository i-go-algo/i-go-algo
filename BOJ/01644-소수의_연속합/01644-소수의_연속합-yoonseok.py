# git commit -m "submit : BOJ 01644 소수의 연속합 (yoonseok)"
MAX = 4000000
N = int(input())
primes = [True]*(MAX+1)
for i in range(2,int(MAX**(1/2))+1):
    for j in range(2*i,MAX+1,i):
        primes[j]=False
primes[0] = False
primes[1] = False
sum = 0
prime_sum = [0]
for i in range(2,MAX+1):
    if primes[i]:
        sum+=i
        prime_sum.append(sum)
left = 0
right = 0
l = len(prime_sum)
answer = 0
while left<=right and right < l:
    if prime_sum[right]-prime_sum[left]==N:
        answer+=1
        right+=1
    elif prime_sum[right]-prime_sum[left]<N:
        right+=1
    elif prime_sum[right]-prime_sum[left]>N:
        left+=1
print(answer)