from collections import deque
q = deque()

n, m = map(int, input().split())
graph = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    q.append([0, 0])
    visited = [[0]*m for _ in range(n)]
    
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny] == 1:
                q.append([nx, ny])
                graph[nx][ny] = graph[x][y] + 1

bfs()
print(graph[n-1][m-1])