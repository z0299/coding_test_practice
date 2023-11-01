import sys

def dfs(now, mustIdx):
    global count
    x = now[0]
    y = now[1]

    if x == must[mustIdx][0] and y == must[mustIdx][1]:
        if mustIdx == m - 1:
            count += 1
            return
        else:
            mustIdx += 1

    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0 and not visited[nx][ny]:
            dfs([nx, ny], mustIdx)
    
    visited[x][y] = 0
    return

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
must = []
for _ in range(m):
    x, y = map(int, input().split())
    must.append([x-1, y-1])
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*n for _ in range(n)]
count = 0

dfs(must[0], 1)
print(count)