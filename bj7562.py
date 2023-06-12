# 7:20 ~ 7:37
from collections import deque

t = int(input())
dir = [[1, 2], [2, 1], [2, -1], [1, -2],
       [-1, -2], [-2, -1], [-2, 1], [-1, 2]]

def bfs(s, e):
    q = deque()
    q.append(s)
    visited = []
    for _ in range(l):
        visited.append([0]*l)
            
    while q:
        x, y = q.popleft()
        if x == e[0] and y == e[1]:
            return visited[x][y]
        for i in range(8):
            nx = x + dir[i][0]
            ny = y + dir[i][1]
            if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1

for _ in range(t):
    l = int(input())
    start = list(map(int, input().split()))
    end = list(map(int, input().split()))
    
    count = bfs(start, end)
    print(count)