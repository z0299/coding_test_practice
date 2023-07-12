from itertools import combinations
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    count = len(idx)
    q = deque(virus)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == 0:
                count -= 1
                visited[nx][ny] = 1
                q.append((nx, ny))
    return count-3

idx = []
virus = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            idx.append((i, j))
        elif board[i][j] == 2:
            virus.append((i, j))

combi = list(combinations(idx, 3))
answer = -1

for c in combi:
    x1, y1 = c[0][0], c[0][1]
    x2, y2 = c[1][0], c[1][1]
    x3, y3 = c[2][0], c[2][1]
    
    board[x1][y1] = 1
    board[x2][y2] = 1
    board[x3][y3] = 1
    
    visited = [[0]*m for _ in range(n)]
    for i in range(len(virus)):
        visited[virus[i][0]][virus[i][1]] = 1
        
    cnt = bfs()
    
    board[x1][y1] = 0
    board[x2][y2] = 0
    board[x3][y3] = 0

    if answer < cnt:
        answer = cnt

print(answer)