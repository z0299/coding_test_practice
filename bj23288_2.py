from collections import deque
q = deque()
n, m, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
board.insert(0, [0]*m)
for i in range(n+1):
    board[i].insert(0, 0)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
score = 0
x, y, dir = 1, 1, 0
dice = [[0, 2, 0],
        [4, 1, 3],
        [0, 5, 0],
        [0, 6, 0]]

count = 0

def move_dice(dir):
    global dice
    if dir == 0:
        tmp = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]]
        dice[3][1] = tmp
    elif dir == 1:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp
    elif dir == 2:
        tmp = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]]
        dice[3][1] = tmp
    else:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
        
def bfs(x, y, C, B):
    visited = [[0]*(m+1) for _ in range(n+1)]
    visited[x][y] = 1
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<nx<=n and 0<ny<=m and board[nx][ny]==B and not visited[nx][ny]:
                C += 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    return C
    
def get_score(x, y):
    global board
    B = board[x][y]
    C = 1
    C = bfs(x, y, C, B)
    return B*C

while True:
    if count == k:
        print(score)
        break
    
    count += 1
    # 1
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0<nx<=n and 0<ny<=m:
        move_dice(dir)
        x, y = nx, ny
    else:
        dir = (dir+2)%4
        move_dice(dir)
        x += dx[dir]
        y += dy[dir]
    
    # 2
    score += get_score(x, y)
    
    #3
    a = dice[3][1]
    b = board[x][y]
    if a > b: dir = (dir+1)%4
    elif a < b: dir = (dir+3)%4