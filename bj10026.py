from collections import deque

n = int(input())
draw = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
q = deque()
not_rg = 0
rg = 0

def bfs(x, y, color):
    q.append([x, y])
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and draw[nx][ny] == color:
                q.append([nx, ny])
                visited[nx][ny] = 1
                if draw[nx][ny] == 'G':
                    draw[nx][ny] = 'R'
                
# 적록색약 아닌사람
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            rg += 1
            bfs(x, y, draw[x][y])
            if draw[x][y] == 'G':
                draw[x][y] = 'R'

visited = [[0]*n for _ in range(n)]
#적록색약인사람
for x in range(n):
    for y in range(n):
        if not visited[x][y]:
            not_rg += 1
            bfs(x, y, draw[x][y])
     
print(rg)            
print(not_rg)