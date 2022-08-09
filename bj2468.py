#완전탐색 알고리즘 공부 - #2468 안전 영역
#DFS, BFS
#DFS로도 풀어보기

import sys
from collections import deque
input = sys.stdin.readline
"""
def DFS(x, y, height):
    visited[x][y] = True
    #print(x,y)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and rain_map[nx][ny] > height and not visited[nx][ny]:
            visited[nx][ny] = True
            print(nx,ny)
            DFS(nx, ny, height)
"""

def BFS(x, y, height):
    queue = deque()
    visited[x][y] = True
    queue.append([x,y])
    
    while queue:
        x, y = queue.popleft()
        #왜 얘를 주석처리 해야 정답이지? 근데 사실 빼도 상관없긴해(어차피 다음 if문에서 걸러주기때문에) 
        #if x == n-1 and y == n-1:
           #return True
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and rain_map[nx][ny] > height and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append([nx, ny])
    

def count_zone(height):
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
    global count
    count = 0
    for i in range(n):
        for j in range(n):
            if not visited[i][j] and rain_map[i][j] > height:
                count += 1
                BFS(i, j, height)
    zone_count.append(count)

n = int(input())
rain_map = []
count = 0
for i in range(n):
    rain_map.append(list(map(int, input().split())))
zone_count = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[0]*(n) for _ in range(n)]
height = [0]
for i in range(n):
    for j in range(n):
        if rain_map[i][j] not in height:
            height.append(rain_map[i][j])
height.sort()

for i in range(len(height)-1):
    count_zone(height[i])

#왜 1하고 비교해서 max값을 해야 정답이지?? max(zone_count)얘로는 정답이 안나옴..
print(max(1, max(zone_count)))