from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*m for _ in range(n)]

def bfs(q):
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0 and not visited[nx][ny]:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append([nx, ny])
                
q = deque()
for x in range(n):
    for y in range(m):
        if tomato[x][y] == 1:
            q.append([x, y])
bfs(q)

day = 0
for i in range(n):
    if 0 in tomato[i]:
        print(-1)
        exit()
        
    day = max(max(tomato[i]), day)

print(day-1)