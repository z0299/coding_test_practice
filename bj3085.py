n = int(input())
board = [list(input()) for _ in range(n)]
ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, visited, color, count):
    visited[x][y] = 1
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == color:
            count += 1
            count = dfs(nx, ny, visited, color, count)
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board [nx][ny] != color:
            for i in range(4):
                nnx = nx + dx[i]
                nny = ny + dy[i]
                if 0<=nnx<n and 0<=nny<n and board[nnx][nny] == color:
                    count += 1
                    return count
                    
    return count
            

# for i in range(n):
#     for j in range(n):
#         visited = [[0]*n for _ in range(n)]
#         count = 0
#         #ans = dfs(i, j, visited, board[i][j], count)
#         ans = dfs(0, 0, visited, board[i][j], count)
#         #ans = max(count, dfs(i, j, visited, board[i][j], count))
        
# print(ans)

# def dfs(x, y, visited, color, count):
#     print(x, y)
#     visited[x][y] = 1
#     count += 1
#     print(count)
    
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and board[nx][ny] == color:
#             count = dfs(nx, ny, visited, color, count)
#     print(count)      
#     return count

# for i in range(n):
#     for j in range(n):
visited = [[0]*n for _ in range(n)]
count = 0
count = dfs(0, 0, visited, board[0][0], count)
print(count)