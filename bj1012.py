# 1:25~
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    global board
    q = deque()
    q.append([x, y])
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1:
                q.append([nx, ny])
                board[nx][ny] = 0
    
t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0]*m for _ in range(n)]
    
    for _ in range(k):
        y, x = map(int, input().split())
        board[x][y] = 1
        
    count = 0
    
    for x in range(n):
        for y in range(m):
            if board[x][y] == 1:
                count += 1
                bfs(x, y)
    print(count)