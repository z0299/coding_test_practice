n = int(input())
board = [list(input().split()) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)]

def dfs(x, y):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if board[nx][ny] == 'S':
                print("NO")
                exit()
            if board[nx][ny] == 'X':
                pass

for x in range(n):
    for y in range(n):
        if board[x][y] == 'T' and not visited[x][y]:
            dfs(x, y)