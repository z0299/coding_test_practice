import sys 
input = sys.stdin.readline
from collections import deque
snake = deque()

n = int(input())
k = int(input())
apple_list = [list(map(int, input().split())) for _ in range(k)]
l = int(input())
dir_list = deque(list(input().split()) for _ in range(l))
board = [[0]*(n+1) for _ in range(n+1)]
snake.append([1, 1])
count = 0
dir = 0
for i in range(k):
    board[apple_list[i][0]][apple_list[i][1]] = -1
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while True:
    count += 1
    
    # 1
    x = snake[-1][0]
    y = snake[-1][1]
    
    nx = x + dx[dir]
    ny = y + dy[dir]
    
    if nx <= 0 or nx >= n+1 or ny <= 0 or ny >= n+1 or ([nx, ny] in snake):
        print(count)
        break
    
    # 2
    elif 0 < nx <= n and 0 < ny <= n and board[nx][ny] == -1:
        board[nx][ny] = 0
        snake.append([nx, ny])
        
    # 3
    elif 0 < nx <= n+1 and 0 < ny <= n+1 and board[nx][ny] == 0:
        snake.append([nx, ny])
        snake.popleft()
        
    # 방향 정보
    if dir_list and int(dir_list[0][0]) == count:
        if dir_list[0][1] == 'D':
            dir = (dir+1)%4
        elif dir_list[0][1] == 'L':
            dir = (dir+3)%4
        dir_list.popleft()
