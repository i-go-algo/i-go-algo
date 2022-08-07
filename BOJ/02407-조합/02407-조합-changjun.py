# git commit -m "submit : BOJ 02407 조합 (changjun)"

# from math import factorial as fact

n, m = map(int, input().split())


# print(fact(n) // (fact(n - m) * fact(m)))

fact = [0] * (n + 2)
fact[0] = 1
fact[1] = 1
for i in range(2, n + 2):
    fact[i] = fact[i - 1] * i
print(fact[n] // (fact[n - m] * fact[m]))
