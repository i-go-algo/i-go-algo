# git commit -m "submit : BOJ 21608 상어 초등학교 (eonyong)"
N = int(input())
N_square = N * N
arr = [[0] * N for _ in range(N)]
numbers = [list(map(int, input().split())) for _ in range(N_square)]
numbers_dict = {}
cnt = 0
answer = 0

while cnt < N_square:
    number, like_numbers = numbers[cnt][0], numbers[cnt][1:]
    numbers_dict[number] = like_numbers
    if not cnt:
        arr[1][1] = number
        cnt += 1
    else:
        tot_yx = []
        for row in range(N):
            for col in range(N):
                if not arr[row][col]:
                    in_box, blank_box = -1, -1
                    for j, i in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
                        nj, ni = row + j, col + i
                        if 0 <= nj < N and 0 <= ni < N:
                            if arr[nj][ni] in like_numbers:
                                in_box += 1
                            elif not arr[nj][ni]:
                                blank_box += 1
                        tot_yx.append([in_box, blank_box, row, col])
        tot_yx.sort(key=lambda x: (x[0], x[1], -x[2], -x[3]))
        _, _, r, c = tot_yx.pop()
        arr[r][c] = number
        cnt += 1

for row in range(N):
    for col in range(N):
        val = 0
        for j, i in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
            nj, ni = row + j, col + i
            if 0 <= nj < N and 0 <= ni < N:
                if arr[nj][ni] in numbers_dict[arr[row][col]]:
                    val += 1
        if val:
            answer += 10 ** (val - 1)
print(answer)


