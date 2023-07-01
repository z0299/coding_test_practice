# 4:10 ~ 4:25
from collections import deque
t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        if visited[x][y] == 'FIRE':
            flag = 'FIRE'
        else:
            flag = visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if board[nx][ny] == '.' and visited[nx][ny] == 0:
                    if flag == "FIRE":
                        visited[nx][ny] = "FIRE"
                    else:
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != "FIRE":
                    return flag
    
    return "IMPOSSIBLE"

for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    q = deque()
    
    for x in range(h):
        for y in range(w):
            if board[x][y] == '*':
                visited[x][y] = 'FIRE'
                q.append((x, y))
            elif board[x][y] == '@':
                start = (x, y)
                visited[x][y] = 1
    
    q.append(start)
    print(bfs())