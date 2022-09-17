# git commit -m "submit : BOJ 14888 연산자 끼워넣기 (eonyong)"
import sys


def Yeonsanza(i, n, numbers, operates, oders, value):
    global maxVal, minVal
    if i == n:
        maxVal, minVal = max(maxVal, int(value)), min(minVal, int(value))
    else:
        for j in range(4):
            if operates[j]:
                operates[j] -= 1
                if value[0] == '-' and j == 3:
                    Yeonsanza(i + 1, n, numbers, operates, oders, f'-{eval(value[1:] + oders[j] + numbers[i])}')
                else:
                    Yeonsanza(i + 1, n, numbers, operates, oders, f'{eval(value + oders[j] + numbers[i])}')
                operates[j] += 1


maxVal, minVal = -float('inf'), float('inf')
N = int(sys.stdin.readline())
numbers = list(sys.stdin.readline().split())
operates = list(map(int, sys.stdin.readline().split()))
oders = ['+', '-', '*', '//']
Yeonsanza(1, N, numbers, operates, oders, f'{numbers[0]}')
print(maxVal)
print(minVal)
