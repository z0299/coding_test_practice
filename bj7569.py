#완전탐색 알고리즘 공부 - #7569 토마토
#3차원 배열 입력받는 법 익히기
#3차원 배열 사용 시 for문 돌리는 순서 z->y->x순이다. 배열 접근 순서 생각해보기!

import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]

def BFS():
    while queue:
        z, y, x = queue.popleft()
        for i in range(6):
            nx = x + dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = tomato[z][y][x] + 1
                queue.append([nz, ny, nx])

m, n, h = map(int, input().split())
tomato = [[(list(map(int,input().split()))) for _ in range(n)] for _ in range(h)]   #3차원 배열 입력받기
queue = deque()
flag = False
date = 0

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k])

BFS()

for i in range(h):
    for j in range(n):
        for k in range(m):
            if tomato[i][j][k] == 0:
                flag = True
            else:
                date = max(date, tomato[i][j][k])
                
if flag:
    print(-1)
else:
    print(date-1)