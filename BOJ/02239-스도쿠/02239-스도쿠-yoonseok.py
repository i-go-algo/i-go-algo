# git commit -m "submit : BOJ 02239 스도쿠 (yoonseok)"
def DFS(depth):
    if depth == len(zeros):     
        return True            

    i, j = zeros[depth]
    r, c = (i // 3) * 3, (j // 3) * 3                
    candidate1 = set(list(range(1, 10)))               
    candidate2 = set(board[i])                    
    candidate2 |= set([board[k][j] for k in range(9)])  
    candidate2 |= set(board[r][c:c + 3])           
    candidate2 |= set(board[r + 1][c:c + 3])         
    candidate2 |= set(board[r + 2][c:c + 3])           
    for num in sorted(candidate1 - candidate2):    
        board[i][j] = num                       
        if DFS(depth + 1):                       
            return True                        
        board[i][j] = 0                           
    return False  
board = [list(map(int, list(input().rstrip()))) for _ in range(9)]
zeros = [(row, col) for row in range(9) for col in range(9) if not board[row][col]]
DFS(0)
for row in board:
    print(*row, sep='')