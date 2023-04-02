# bfs 알고리즘 공부 - 

from collections import deque
queue = deque()
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(maze, visited, x, y):
    visited[x][y] = 1
    queue.append([x, y])
    
    while queue:
        x, y = queue.popleft()
        if x == n-1 and y == m-1:
            print(visited[x][y])
            print(visited)
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 6 and not visited[nx][ny] and maze[nx][ny] == 1:
                queue.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

n, m = map(int, input().split())
maze = []
for i in range(n):
    maze.append(list(map(int, input())))
visited = [[0]*m for _ in range(n)]

BFS(maze, visited, 0, 0)