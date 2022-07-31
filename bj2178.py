#완전탐색 알고리즘 공부 - #2178 미로탐색
#DFS
#DFS는 구현했는데 여러 루트중에 가장 최소 경유 루트 찾아내는 방법을 모르겠음
#왜 BFS로 구현하는 문제인가? 두 노드간 최단경로 찾을 때 사용
import sys
from collections import deque

"""
두 노드 사이의 최단경로를 찾기 때문에 BFS를 사용하는 문제였음...
def DFS(x, y, count):
    count += 1
    visited[x][y] = True
    for _ in range(1, n*m):
        print(x, y, count)
        if x == n-1 and y == m-1:
            print(count)
            exit()
        elif y+1 <= m-1 and not visited[x][y+1] and maze[x][y+1] == 1:
            DFS(x, y+1, count)
        elif x+1 <= n-1 and not visited[x+1][y] and maze[x+1][y] == 1:
            DFS(x+1, y, count)
        elif x-1 >= 0 and not visited[x-1][y] and maze[x-1][y] == 1:
            DFS(x-1, y, count)
        else:
            return(x+1, y+1, count)
"""

def BFS():
    queue = deque()
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    visited[0][0] = 1
    queue.append([0,0])
    
    while queue:
        x, y = queue.popleft() #popleft: 처음 들어간 것 부터 값을 뺀다(선입선출)
        #print(x,y)
        if x == n-1 and y == m-1:
            print(visited[x][y])
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m: 
                if visited[nx][ny] == 0 and maze[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append([nx,ny])
                
n, m = map(int, sys.stdin.readline().split())
maze = []
for i in range(n):
    maze.append(list(map(int, sys.stdin.readline().rstrip())))  #rstrip: 공백없는 문자열 분리
visited = [[0]*m for _ in range(n)]

BFS()
"""
finish_point = [0,0]
while finish_point[0] != n-1 and finish_point[1] != m-1:
    count = 0
    finish_point[0], finish_point[1], count = DFS(finish_point[0], finish_point[1], count)
"""