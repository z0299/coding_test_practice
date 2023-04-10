from collections import deque
q = deque()
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
total_score = 0
x, y, dir = 0, 0, 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dice = [[0, 2, 0],
        [4, 1, 3],
        [0, 5, 0],
        [0, 6, 0]]

def move_once(x, y, dir):
    global dice
    nx = x + dx[dir]
    ny = y + dy[dir]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        dir = (dir+2)%4
        nx = x+dx[dir]
        ny = y+dy[dir]
    x, y = nx, ny
    
    # move_dice
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
    return x, y, dir

def bfs(x, y, c, b):
    q.append([x, y])
    visited = [[0]*m for _ in range(n)]
    visited[x][y] = 1
    c += 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == b:
                q.append([nx, ny])
                c += 1
                visited[nx][ny] = 1
    return c

def get_score(x, y):
    b = board[x][y]
    c = 0
    c = bfs(x, y, c, b)
    return b*c

count = 0
while True:
    if count == k:
        print(total_score)
        break
    count += 1
    # 실행
    # 1
    x, y, dir = move_once(x, y, dir)
    # 2
    total_score += get_score(x, y)
    # 3
    a = dice[3][1]
    b = board[x][y]
    if a > b: dir = (dir+1)%4
    elif a < b: dir = (dir+3)%4
