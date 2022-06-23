# git commit -m "submit: BOJ 01003 피보나치 함수 (changjun)"

t = int(input())
lst0 = [0]*41
lst1 = [0]*41

lst0[0] = 1
lst0[2] = 1

lst1[1] = 1
lst1[2] = 1
for i in range(2,41):
    lst0[i] = lst0[i-1] + lst0[i-2]
    lst1[i] = lst1[i-1] + lst1[i-2]

for case in range(t):
    n = int(input())
    print(lst0[n], lst1[n])

