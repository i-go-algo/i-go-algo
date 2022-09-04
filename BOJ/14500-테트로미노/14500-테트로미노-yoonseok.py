# git commit -m "submit : BOJ 14500 테트로미노 (yoonseok)"
tetrominos = [
    [[1,1,1,1]],

    [[1,1],
    [1,1]],

    [[1,0],
    [1,0],
    [1,1]],

    [[1,0],
    [1,1],
    [0,1]],

    [[1,1,1],
    [0,1,0]],
]

def rot(tetromino):
    r = len(tetromino)
    c = len(tetromino[0])
    res = [[0]*r for _ in range(c)]
    #print(res)
    for i in range(r):
        for j in range(c):
            #print(tetromino)
            #print(r-i-1, r)
            res[j][r-i-1] = tetromino[i][j]
    return res

def mirror(tetromino):
    r = len(tetromino)
    c = len(tetromino[0])
    res = [[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            res[i][c-j-1] = tetromino[i][j]
    return res

N, M = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]
answer = 0
for tetromino in tetrominos:
    for i in range(4):
        tetromino = rot(tetromino)
        tr = len(tetromino)
        tc = len(tetromino[0])
        #for _ in range(tr):
        #    print(tetromino[_])
        #print('-----------------------')
        for i in range(N-tr+1):
            for j in range(M-tc+1):
                temp = 0
                for k in range(tr):
                    for l in range(tc):
                        if tetromino[k][l]:
                            temp+=board[i+k][j+l]
                answer = max(answer,temp)
    tetromino = mirror(tetromino)
    for i in range(4):
        tetromino = rot(tetromino)
        tr = len(tetromino)
        tc = len(tetromino[0])
        #for _ in range(tr):
        #    print(tetromino[_])
        #print('-----------------------')
        for i in range(N-tr+1):
            for j in range(M-tc+1):
                temp = 0
                for k in range(tr):
                    for l in range(tc):
                        if tetromino[k][l]:
                            temp+=board[i+k][j+l]
                answer = max(answer,temp)
print(answer)