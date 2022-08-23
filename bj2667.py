#완전탐색 알고리즘 공부 - #2667 단지번호붙이기
#BFS
#DFS로도 풀 수 있음
import sys
from collections import deque
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
#count = 1

def BFS(x,y):
    queue = deque()
    count = 1
    queue.append([x,y])
    
    #단지 찾기
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and houses_map[nx][ny] == 1 and not houses_visited[nx][ny]:
                queue.append([nx,ny])
                houses_visited[nx][ny] = True
                houses_map[nx][ny] == 0
                count += 1
    #단지 내 집 수 return
    return(count)

"""
def DFS(x,y):
    global count
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and houses_map[nx][ny] == 1 and not houses_visited[nx][ny]:
            count += 1
            houses_visited[nx][ny] = True
            houses_map[nx][ny] == 0
            DFS(nx, ny)
"""
            
#입력받기
n = int(input())
houses_map = []
houses_list = []
for _ in range(n):
    houses_map.append(list(map(int, input().rstrip())))
houses_visited = [[False]*n for _ in range(n)]

#단지 수 만큼 돌며 단지 내 집 수 찾기
#각 단지의 첫번째 집(출발점) 찾기
for i in range(n):
    for j in range(n):
        if houses_map[i][j] == 1 and not houses_visited[i][j]:
            houses_visited[i][j] = True
            houses_map[i][j] = 0
            houses_num = BFS(i,j)
            houses_list.append(houses_num)
            """
            DFS(i,j)
            houses_list.append(count)
            count = 1
            """

#출력
print(len(houses_list))
houses_list.sort()
for i in houses_list:
    print(i)