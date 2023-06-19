# 4:45 ~
from copy import deepcopy

r, c, t = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]
time = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

check = "top"
# 공기청정기 위치 확인
for x in range(r):
    for y in range(c):
        if board[x][y] == -1:
            if check == "top":
                top = x
                check = "down"
            elif check == "down":
                down = x

while time < t:
    time += 1
    
    # 미세먼지 확산
    temp_board = [[0]*c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if board[x][y] > 0:
                dust = board[x][y] // 5
                count = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] != -1:
                        count += 1
                        temp_board[nx][ny] += dust
                
                temp_board[x][y] -= dust*count
    
    for x in range(r):
        for y in range(c):
            board[x][y] += temp_board[x][y]  
            
    # 공기청정기 작동
    new_board = deepcopy(board)
    
    # 윗 부분 - 아래
    for col in range(1, c):
        if col == 1:
            new_board[top][col] = 0
        else:
            new_board[top][col] = board[top][col-1]     
         
    # 윗 부분 - 오른쪽
    for row in range(top, -1, -1):
        if row == top:
            new_board[row][c-1] = board[row][c-2]
        else:
            new_board[row][c-1] = board[row+1][c-1]
    
    # 윗 부분 - 위
    for col in range(c-2, -1, -1):
        new_board[0][col] = board[0][col+1]
        
    # 윗 부분 - 왼쪽
    for row in range(1, top):
        new_board[row][0] = board[row-1][0]
            
    # 아랫 부분 - 위
    for col in range(1, c):
        if col == 1:
            new_board[down][col] = 0
        else:
            new_board[down][col] = board[down][col-1]

    # 아랫 부분 - 오른쪽
    for row in range(down+1, r):
        new_board[row][c-1] = board[row-1][c-1]
    
    # 아랫 부분 - 아래
    for col in range(c-2, -1, -1):
        new_board[r-1][col] = board[r-1][col+1]
    
    # 아랫 부분 - 왼쪽
    for row in range(r-2, down-1, -1):
        new_board[row][0] = board[row+1][0]
        
    new_board[top][0] = -1
    new_board[down][0] = -1
    board = new_board
    
    
answer = 0    
# 합계 구하기
for i in range(len(board)):
    answer += sum(board[i])
print(answer+2)
        
        
        