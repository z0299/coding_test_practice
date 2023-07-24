import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
blocks = [list(map(int, input().split())) for _ in range(k)]

board = [[0]*n for _ in range(m)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for b in blocks:
    x1, y1, x2, y2 = b[0], b[1], b[2],b [3]
    for x in range(x1, x2):
        for y in range(y1, y2):
            board[y][x] = 1

def dfs(x, y):
    global temp
    temp += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
            board[nx][ny] = 1
            dfs(nx, ny)
    return 

count = 0      
width = []
for x in range(m):
    for y in range(n):
        if board[x][y] == 0:
            count += 1
            board[x][y] = 1
            temp = 0
            dfs(x, y)
            width.append(temp)
            
print(count)
for n in sorted(width):
    print(n, end=' ')