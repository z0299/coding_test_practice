from collections import deque
from itertools import combinations

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
"""
def bfs(x, y):
    q = deque()
    q.append((x, y, 0))
    visited = [[0]*n for _ in range(n)]
    visited[x][y] = 1
    chicken_len = []
    
    while q:
        if len(chicken_len) == len(house):
            return chicken_len
        
        x, y, count = q.popleft()
        # print(x, y, count)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if board[nx][ny] == 1:
                    chicken_len.append([count+1, (nx, ny)])
                q.append((nx, ny, count+1))
                visited[nx][ny] = 1
"""
chicken = []
house = []
for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            house.append((x, y))
        elif board[x][y] == 2:
            chicken.append((x, y))
            
combi = list(combinations(chicken, m))
answer = 99999
for c in combi:
    total = 0
    for h in house:
        # print(h)
        temp = 9999
        for i in range(m):
            temp = min(temp, abs(h[0] - c[i][0]) + abs(h[1] - c[i][1]))
        total += temp
    answer = min(answer, total)
print(answer)

"""
chicken_lens = []           
for i in range(len(chicken)):
    chicken_len = bfs(chicken[i][0], chicken[i][1])
    chicken_lens.append(chicken_len)
print(chicken_lens)
"""