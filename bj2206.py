# 6:40 ~
"""
import sys
sys.setrecursionlimit(10000000)

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
breaked = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*m for _ in range(n)]
count = []

def dfs(x, y, breaked):
    if x == n-1 and y == m-1:
        count.append(visited[n-1][m-1])
        return count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] != 1 and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, breaked)
            visited[nx][ny] = 0
        elif 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not breaked and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            breaked = 1
            dfs(nx, ny, breaked)
            breaked = 0
            visited[nx][ny] = 0
    
    return

visited[0][0] = 1
dfs(0, 0, breaked)
if count:
    print(min(count))
else:
    print(-1)
"""
"""
from collections import deque

n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*m for _ in range(n)]

def bfs(x, y):
    q = deque()
    q.append([x, y, 0])
    visited[x][y] = 1
    while q:
        x, y, breaked = q.popleft()
        print(x, y, breaked)
        print(visited)
        if x == n-1 and y == m-1:
            print(visited)
            return visited[n-1][m-1]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny, breaked])
            elif 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and not breaked and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny, 1])

count = bfs(0, 0)
if count == None:
    print(-1)
else:
    print(count)
"""
from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input())) for _ in range(n)]
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solve(x, y, wall_break_left, visited, board):
    q = deque()
    q.append((x, y, wall_break_left))
    visited[x][y][wall_break_left] = 1
    while q:
        x, y, wall_break_left = q.popleft()
        if x == n-1 and y == m-1:
            return visited[x][y][wall_break_left]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0 and visited[nx][ny][wall_break_left] == 0:
                q.append((nx, ny, wall_break_left))
                visited[nx][ny][wall_break_left] = visited[x][y][wall_break_left]+1
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 1 and wall_break_left == 1:
                q.append((nx, ny, wall_break_left -1))
                visited[nx][ny][wall_break_left-1] = visited[x][y][wall_break_left]+1
    return -1

print(solve(0, 0, 1, visited, board))
        