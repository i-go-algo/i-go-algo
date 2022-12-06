# git commit -m "submit : BOJ 01806 부분합 (eonyong)"

import sys

input = sys.stdin.readline

n, m = map(int, input().split())
ls = list(map(int, input().split()))

for val in ls:
    # 만약, 입력 받은 값 중에서 m 이상인 값이 있으면 1을 출력하고 끝
    if val >= m:
        print(1)
        break
else:
    answer = float('inf')
    # 투 포인터를 사용하기 위해 start와 end를 지정해줍니다.
    s, e = 0, 1
    # 미리 두 값을 더한 value를 생성해줍니다.
    value = ls[s] + ls[e]

    while s < n and e < n:
        # value가 m보다 작으면 end점을 늘려가며 값을 더하고 인덱스 n까지 간 경우에는 거리 최솟값을 비교하고 break
        if value < m:
            e += 1
            if e == n:
                answer = min(answer, e - s + 1)
                break
            value += ls[e]
        else:
            # value가 m 이상인 경우에는 start점을 키우면서 값을 뺴면서 최소 길이를 구해준다.
            answer = min(answer, e - s + 1)
            value -= ls[s]
            s += 1
        # 만약, start점과 end점이 같으면 break
        if s == e:
            break

    if s == 0 and e == n:  # 끝까지 탐색을 했지만 조건에 맞는 길이가 없는 경우
        print(0)
    else:
        print(answer)
