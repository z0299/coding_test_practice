from collections import deque

n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
UP, LEFT, DOWN, RIGHT = 0, 1, 2, 3
dir = RIGHT
dice = [[0,2,0],
        [4,1,3],
        [0,5,0],
        [0,6,0]]

def move_dice(dir):
    global dice
    if dir == RIGHT:
        tmp = dice[1][2]
        dice[1] = [dice[3][1], dice[1][0], dice[1][1]]
        dice[3][1] = tmp
    elif dir == LEFT:
        tmp = dice[1][0]
        dice[1] = [dice[1][1], dice[1][2], dice[3][1]]
        dice[3][1] = tmp
    elif dir == UP:
        tmp = dice[0][1]
        dice[0][1] = dice[1][1]
        dice[1][1] = dice[2][1]
        dice[2][1] = dice[3][1]
        dice[3][1] = tmp
    elif dir == DOWN:
        tmp = dice[3][1]
        dice[3][1] = dice[2][1]
        dice[2][1] = dice[1][1]
        dice[1][1] = dice[0][1]
        dice[0][1] = tmp

def get_score_by_bfs(sy, sx, b):
    used = [[False]*m for _ in range(n)]    # 방문 확인용 배열
    cnt = 0
    q = deque()
    q.append((sy, sx))
    used[sy][sx] = True
    while q:
        y, x = q.pop()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if ny < 0 or nx < 0 or ny >= n or nx >= m or used[ny][nx]:
                continue
            if board[ny][nx] == b:
                used[ny][nx] = True
                q.append((ny, nx))
    return cnt*b

loc = (0, 0)
result = 0

for i in range(k):
    ny = loc[0]+dy[dir]
    nx = loc[1] + dx[dir]
    
    if ny < 0 or nx < 0 or ny >= n or nx >= m: # 이동할 수 없는 경우
        dir = (dir + 2) % 4 # 방향을 180도 바꿔서 이동
        ny = loc[0] + dy[dir]
        nx = loc[1] + dx[dir]
    loc = (ny, nx)
    move_dice(dir)
    b = board[ny][nx]
    score = get_score_by_bfs(ny, nx, b)
    result += score
    
    a = dice[3][1]
    if a > b: dir = (dir-1)%4
    elif a < b: (dir + 1)%4
print(result)