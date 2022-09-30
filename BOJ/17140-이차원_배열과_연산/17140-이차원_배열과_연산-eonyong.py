# git commit -m "submit : BOJ 17140 이차원 배열과 연산 (eonyong)"
import sys
from collections import defaultdict
input = sys.stdin.readline


# 각 연산 수행
def SortingArray(array, l, flag):
    # 최대 길이 초기화
    max_l = l
    nxt_numbers = []
    for arr in array:
        nxt = []
        numbers = defaultdict(int)
        for number in arr:
            # 0이 아닌 수의 값 갯 수 저장
            if number:
                numbers[number] += 1
        
        # 숫자의 개수, 숫자 오름차순으로 정렬
        numbers = sorted(map(list, numbers.items()), key=lambda x: (x[1], x[0]))
        for number in numbers:
            nxt += number

        # 최대 길이 업데이트
        max_l = max(max_l, len(nxt))

        # 각 행 nxt_numbers에 저장
        nxt_numbers.append(nxt)
    if flag:
        # C연산 -> 뒤집은 boards와 최대 길이 반환
        return list(map(list, zip(*[nxt_number + [0] * (max_l - len(nxt_number)) for nxt_number in nxt_numbers]))), max_l
    else:
        # R연산 -> boards와 최대 길이 반환
        return [nxt_number + [0] * (max_l - len(nxt_number)) for nxt_number in nxt_numbers], max_l


r, c, k = map(int, input().split())
h, w = 3, 3
boards = [list(map(int, input().split())) for _ in range(3)]

# 시간측정 변수
cnt = 0
while cnt <= 100:
    if h >= r and w >= c and boards[r - 1][c - 1] == k:
        # borads[r - 1][c - 1] 위치에 k값이 존재하면 걸린 시간 출력하고 while 탈출
        print(cnt)
        break
    if h >= w:
        # R연산
        boards, w = SortingArray(boards, w, 0)
    else:
        # C연산 -> boards를 뒤집어서 함수에 넣어줘야함
        boards, h = SortingArray(list(map(list, zip(*boards))), h, 1)
    cnt += 1
else:
    # 100초가 지났음에도 결과가 안나오면 -1 출력
    print(-1)
