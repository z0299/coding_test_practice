# gravity 못만들었고, 90도 돌리는거 좀 이상하다.

from collections import deque
q = deque()
n, m = map(int, input().split())
board = [list((map(int, input().split()))) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_score = 0

def bfs(x, y, c):
    rainbow, count, std_row, std_col = 0, 0, 0, 0
    q.append([x, y])
    count += 1
    std_row = x
    std_col = y
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                # 무지개 블럭인 경우
                if board[nx][ny] == 0:
                    count += 1
                    rainbow += 1
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    if nx < std_row: std_row = nx
                    if ny < std_col: std_col = ny
                # 블럭이 일반인 경우
                elif board[nx][ny] == c:
                    count += 1
                    q.append([nx, ny])
                    visited[nx][ny] = 1
                    if nx < std_row: std_row = nx
                    if ny < std_col: std_col = ny
                else: continue
    return visited, count, rainbow, std_row, std_col                   

def find_block_group():
    block_group = []
    block_size = 0
    rainbow_count = 0
    std_row, std_col = 0, 0
    
    for x in range(n):
        for y in range(n):
            if board[x][y] and board[x][y] != -1:
                temp_group = []
                temp_size, temp_rainbow = 0, 0
                color = board[x][y]
                temp_group, temp_size, temp_rainbow, std_row, std_col = bfs(x, y, color)
            if block_size < temp_size:
                block_group = temp_group
                block_size = temp_size
                rainbow_count = temp_rainbow
            elif block_size == temp_size:
                if rainbow_count < temp_rainbow:
                    block_group = temp_group
                    block_size = temp_size
                    rainbow_count = temp_rainbow
                elif rainbow_count == temp_rainbow:
                    if x < std_row:
                        block_group = temp_group
                        block_size = temp_size
                        rainbow_count = temp_rainbow
                    elif x == std_row:
                        if y == std_col:
                            block_group = temp_group
                            block_size = temp_size
                            rainbow_count = temp_rainbow
    if block_size == 0:
        return 0, 0
    else:
        return block_group, block_size
                
def delete_block_group(block_group):
    global board
    for x in range(n):
        for y in range(n):
            if block_group[x][y] == 1:
                board[x][y] = -2
                
def gravity(board):
    # for y in range(n):
    #     end = n
    #     for x in range(n):
    #         if type(board[x][y]) is int:
    #             if board[x][y] >= 0:
    #                 start = x
    #             if board[x][y] == -1:
    #                 end = x
    #     # if start == 0 and end == n:
    #     #     continue
    #     if board[start][y] != '0':
    #         board[end-1][y] = board[start][y]
    #         while start < end-1:
    #             board[start][y] = '0'
    #             start += 1
    # print(board)
    for i in range(n-1, -1, -1): # 밑에서 부터 체크
        for j in range(n):
            if type(board[i][j]) is int:
                if board[i][j] > -1: # -1이 아니면 아래로 다운
                    r = i
                    while True:
                        if 0 <= r+1 < n and board[r+1][j] == -2: # 다음 행이 인덱스 범위 안이면서 -2이면 아래로 다운
                            board[r+1][j] = board[r][j]
                            board[r][j] = -2
                            r += 1
                        else:
                            break

def rotate_90():
    temp_board = [[0]*n for _ in range(n)]
    for x in range(n):
        for y in range(n):
            temp_board[x][y] = board[n-y-1][x]
    return temp_board

while True:
    # 블록그롭 찾기
    block_group, score = find_block_group()
    if block_group == 0:
        print(total_score)
        exit()
    # 블록 제거
    delete_block_group(block_group)
    # 점수 획득
    total_score += score*score
    # 중력 작용
    gravity(board)
    board = rotate_90()
    gravity(board)
    print(board)
