# git commit -m "submit : BOJ 17142 연구소 3 (eonyong)"
import sys
from collections import deque

input = sys.stdin.readline


# 바이러스가 퍼지는 과정
def Diffusions(virus, boards, visited, N, zero):
    value, cnt = 0, 0

    while virus:
        row, col = virus.popleft()
        for j, i in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            nj, ni = row + j, col + i
            # 벽이 아닌 부분에 확산을 진행
            if 0 <= nj < N and 0 <= ni < N and boards[nj][ni] != 1 and visited[nj][ni] == -1:
                visited[nj][ni] = visited[row][col] + 1
                virus.append([nj, ni])
                # 값이 0이면 최댓값 업데이트 진행, 2인 경우에는 그냥 활성화만 되기 때문에 업데이트를 하지 않는다.
                if not boards[nj][ni]:
                    # 0의 갯수를 세는 cnt + 1 해준다
                    cnt += 1
                    value = max(value, visited[nj][ni])
    
    # cnt가 초기 0의 갯수인 zero와 같다면 value 반환, 아니면 무한대값 반환
    if cnt == zero:
        return value
    else:
        return float('inf')


# M개를 뽑아내는 combinations 과정
def SelectM(i, k, N, M, boards, viruses, arr, zero):
    global answer
    if i == M:
        visited = [[-1 for _ in range(N)] for _ in range(N)]
        # 선택된 바이러스 자리에 초기값 0을 입력
        for r, c in viruses:
            visited[r][c] = 0
        # 확산이 다 된 값과 answer를 비교하여 최솟값 도출, Diffusion 진행
        answer = min(answer, Diffusions(deque(arr), boards, visited, N, zero))
    else:
        for j in range(k, len(viruses)):
            if viruses[j] not in arr:
                arr.append(viruses[j])
                SelectM(i + 1, j, N, M, boards, viruses, arr, zero)
                arr.pop()


answer = float('inf')
n, m = map(int, input().split())
viruses, boards, zero = [], [], 0
# 입력을 받으면서 바이러스의 위치와 0의 개수 업데이트
for row in range(n):
    ls = list(map(int, input().split()))
    for col in range(n):
        if ls[col] == 2:
            viruses.append([row, col])
        if not ls[col]:
            zero += 1
    boards.append(ls)

# combinations 시작
SelectM(0, 0, n, m, boards, viruses, [], zero)
# 만약 answer가 float('inf')이면 -1 아니면 answer 출력
if answer == float('inf'):
    print(-1)
else:
    print(answer)
