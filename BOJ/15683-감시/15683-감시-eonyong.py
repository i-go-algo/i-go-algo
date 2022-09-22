# git commit -m "submit : BOJ 15683 감시 (eonyong)"

# 각 CCTV 방식으로 탐색하면서 6을 찾으면 return
def FindSix(nj, ni, i, j):
    cnt, position = 0, []
    while True:
        ni, nj = ni + i, nj + j
        if 0 <= nj < N and 0 <= ni < M:
            if not places[nj][ni]:
                cnt += 1
                position.append([nj, ni])
            elif places[nj][ni] == 6:
                return cnt, position
        else:
            return cnt, position


def CCTV(arr, tot, idx):
    global ans
    if idx < len(arr):
        num, row, col = arr[idx]
        # 1번 CCTV로 감시할 경우
        if num == 1:
            
            # 탐색된 장소를 -1로 체크
            for i, j in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                cnt, position = FindSix(row, col, i, j)
                # 탐색된 장소를 -1로 체크
                for r, c in position:
                    places[r][c] = -1
                CCTV(arr, tot - cnt, idx + 1)
                
                # 원상복귀
                for r, c in position:
                    places[r][c] = 0
        # 2번 CCTV로 감시할 경우
        elif num == 2:
            
            # 탐색된 장소를 -1로 체크
            for i, j in [[0, 1], [1, 0]]:
                cnt1, position1 = FindSix(row, col, i, j)
                cnt2, position2 = FindSix(row, col, -i, -j)
                cnt, position = cnt1 + cnt2, position1 + position2
                
                # 탐색된 장소를 -1로 체크
                for r, c in position:
                    places[r][c] = -1
                CCTV(arr, tot - cnt, idx + 1)
            
                # 원상복귀
                for r, c in position:
                    places[r][c] = 0

        # 3번 CCTV로 감시할 경우
        elif num == 3:
            
            # 탐색된 장소를 -1로 체크
            for i, j in [[1, 1], [1, -1], [-1, 1], [-1, -1]]:
                cnt1, position1 = FindSix(row, col, i, 0)
                cnt2, position2 = FindSix(row, col, 0, j)
                cnt, position = cnt1 + cnt2, position1 + position2
                
                # 탐색된 장소를 -1로 체크
                for r, c in position:
                    places[r][c] = -1
                
                CCTV(arr, tot - cnt, idx + 1)
                
                # 원상복귀
                for r, c in position:
                    places[r][c] = 0

        # 4번 CCTV로 감시할 경우
        elif num == 4:
            
            # 탐색된 장소를 -1로 체크
            for rot in [[[-1, 0], [0, -1], [0, 1]], [[-1, 0], [1, 0], [0, 1]], [[1, 0], [0, -1], [0, 1]],
                        [[-1, 0], [0, -1], [1, 0]]]:
                cnt, position = 0, []
                for i, j in rot:
                    cnt1, position1 = FindSix(row, col, i, j)
                    cnt, position = cnt + cnt1, position + position1

                # 탐색된 장소를 -1로 체크
                for r, c in position:
                    places[r][c] = -1
                
                CCTV(arr, tot - cnt, idx + 1)
                
                # 원상복귀
                for r, c in position:
                    places[r][c] = 0

        # 5번 CCTV로 감시할 경우
        elif num == 5:
            cnt, position = 0, []
            
            # 탐색한 장소와 갯수를 구해서 cnt에 저장
            for i, j in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                cnt1, position1 = FindSix(row, col, i, j)
                cnt, position = cnt + cnt1, position + position1

            # 탐색된 장소를 -1로 체크
            for r, c in position:
                places[r][c] = -1
                
            CCTV(arr, tot - cnt, idx + 1)
            
            # 원상복귀
            for r, c in position:
                places[r][c] = 0
    else:
        if ans > tot:
            ans = tot


cctv = []
answer = 0

N, M = map(int, input().split())
ans = N * M

places = [[0] * M for _ in range(N)]

for row in range(N):
    ls = list(map(int, input().split()))
    for col in range(M):
        places[row][col] = ls[col]
        if 0 < ls[col] < 6:
            cctv.append([ls[col], row, col])
        elif not ls[col]:
            answer += 1

cctv.sort(key=lambda x: x[0])

CCTV(cctv, answer, 0)

print(ans)
