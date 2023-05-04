from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*m for _ in range(n)]
draw = 0
max_draw = 0

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = 1
    wide = 0
    
    while q:
        x, y = q.popleft()
        wide += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = 1
    return wide      

for x in range(n):
    for y in range(m):
        if board[x][y] == 1 and not visited[x][y]:
            draw += 1
            temp = bfs(x, y)
            if temp > max_draw:
                max_draw = temp

if draw > 0:
    print(draw)
    print(max_draw)
else:
    print(draw)
    print(0)