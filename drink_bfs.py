# bfs 알고리즘 공부 - 1시간^^..

from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(ice, visited, x, y):

    queue.append([x, y])
    visited[x][y] = 1
    
    while queue:
        x, y = queue.popleft()
        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 4 and 0 <= ny < 5 and ice[nx][ny] == 0 and not visited[nx][ny]:
                visited[nx][ny] = 1
                queue.append([nx, ny])

n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input())))
queue = deque()
visited = [[0]*(m) for _ in range(n)]
count = 0

for i in range(n):
    for j in range(m):
        if ice[i][j] == 0 and not visited[i][j]:
            count += 1
            bfs(ice, visited, i, j)
print(count)