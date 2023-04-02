#완전탐색 알고리즘 공부 - #2573 빙산

import sys
from collections import deque

#인접 0 개수 세기
def num_of_zeros(x, y):
    num_of_zero = 0
    
    for i in range(4):
        zx = x + dx[i]
        zy = y + dy[i]
        if glacier_map[zx][zy] == 0:
            num_of_zero += 1
            
    return(num_of_zero)

#zone 개수 세기
def count_zone(i,j, year):
    year += 1
    zeros = []
    queue = deque()
    queue.append([i, j])
    visited[i][j] = 1
    
    while queue:
        x, y = queue.popleft()
        zeros = num_of_zeros(x, y)
        #print(x, y, zeros, glacier_map[x][y]-zeros)
        if glacier_map[x][y] - zeros > 0:
            glacier_map[x][y] = glacier_map[x][y] - zeros
        elif glacier_map[x][y] - zeros <= 0:
            glacier_map[x][y] = -1
            
        #print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if glacier_map[nx][ny] > 0 and visited[nx][ny] == False:
                queue.append([nx, ny])
                visited[nx][ny] = 1    

#main 시작
input = sys.stdin.readline
n, m = map(int, input().split())
glacier_map = []

for i in range(n):
    glacier_map.append(list(map(int, input().split())))
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
year = -1
visited = [[0]*m for _ in range(n)]

#visited 맵에서 갈 수 없는 곳(바다) 표기
for i in range(n):
    for j in range(m):
        if glacier_map[i][j] == 0:
            visited[i][j] = 1

#빙산이 나오면 zone 개수 세기
for i in range(n):
    for j in range(m):
        if glacier_map[i][j] > 0 and visited[i][j] == False:
            #print("here")
            count += 1
            count_zone(i, j, year)
            
print(glacier_map)
            
print(count)