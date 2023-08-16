# 7:35 ~
from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
# print(board)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    side = set()
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
                q.append((nx, ny))
                for j in range(4):
                    nnx = nx + dx[j]
                    nny = ny + dy[j]
                    if 0 <= nnx < n and 0 <= nny < n and board[nnx][nny] == 0:
                        side.add((nx, ny))
    return side

            
islands = []
for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            temp = bfs(x, y)
            print(temp)