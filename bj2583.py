# 8:00 ~
import sys
sys.setrecursionlimit(10000)

m, n, k = map(int, input().split())
axis = [list(map(int, input().split())) for _ in range(k)]
board = [[0]*n for _ in range(m)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, count):
    board[x][y] = 1
    count += 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<m and 0<=ny<n and board[nx][ny] == 0:
            count = dfs(nx, ny, count)
    return count
    
# 직사각형 그리기
for i in range(k):
    x_start, y_start = axis[i][0], axis[i][1]
    x_end, y_end = axis[i][2], axis[i][3]
    
    for y in range(y_start, y_end):
        for x in range(x_start, x_end):
            board[y][x] = 1

# dfs           
area_list = []
for i in range(n):
    for j in range(m):
        if board[j][i] == 0:
            area_count = 0
            area_count = dfs(j, i, area_count)
            area_list.append(area_count)
            
print(len(area_list))
area_list.sort()
for i in range(len(area_list)):
    print(area_list[i], end=' ')