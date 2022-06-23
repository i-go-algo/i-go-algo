# git commit -m "submit : BOJ 01003 피보나치 함수 (eonyong)"
for _ in range(int(input())):
    n = int(input())
    # n이 0이면
    if n == 0:
        print(1, 0)
    # n이 1이면
    elif n == 1:
        print(0, 1)
    # 그 외의 경우
    else:
        arr = [1, 1]
        for idx in range(2, n):
            arr.append(arr[idx - 1] + arr[idx - 2])
        print(*arr[-2:])
