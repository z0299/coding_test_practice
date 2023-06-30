# 4:05 ~
"""
from collections import deque

t = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(board, sg):
    q = deque()
    visited = [[0]*w for _ in range(h)]
    q.append(sg)
    route = []
    while q:
        x, y = q.popleft()
        visited[x][y] = 1
        
        if x == 0 or x == h-1 or y == 0 or y == w-1:
            break
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] == '.' and not visited[nx][ny]:
                q.append([nx, ny])
                if i == 0:
                    route.append([nx, ny, 'U'])
                elif i == 1:
                    route.append([nx, ny, 'D'])
                elif i == 2:
                    route.append([nx, ny, 'L'])
                else:
                    route.append([nx, ny, 'R'])
    
    return route        
            
    

for _ in range(t):
    w, h = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    count = 1
    
    # 상근이 위치 저장 및 불 번지기
    new_fire = []
    for x in range(h):
        for y in range(w):
            if board[x][y] == '*':
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < h and 0 <= ny < w:
                        if board[nx][ny] == '@':
                            sg = [nx, ny]
                            new_fire.append([nx, ny])
                        elif board[nx][ny] == '#':
                            continue
                        else:
                            new_fire.append([nx, ny])
                        
            elif board[x][y] == '@':
                sg = [x, y]
                board[x][y] = '.'
    
    # 불 번지기
    for i in range(len(new_fire)):
        board[new_fire[i][0]][new_fire[i][1]] = '*'
        
    # 상근이 옮기기
    route = bfs(board, sg)
    print(route)
    
    print(board, sg)
    
    """
from collections import deque 
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    while q:
        x, y = q.popleft()
        if visited[x][y] != 'FIRE':
            flag = visited[x][y]
        else:
            flag = "FIRE"

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < h and 0 <= ny < w:
                if visited[nx][ny] == 0 and board[nx][ny] == '.':
                    if flag == 'FIRE':      # 불인 경우
                        visited[nx][ny] = flag
                    else:                   # 불이 아닌 경우
                        visited[nx][ny] = flag + 1
                    q.append((nx, ny))
            else:
                if flag != 'FIRE':
                    return flag
                
    return "IMPOSSIBLE"

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        w, h = map(int, input().split())
        q = deque()
        board = []
        visited = [[0]*w for _ in range(h)]
        
        for i in range(h):
            board.append(list(input()))
            for j in range(w):
                if board[i][j] == '@':
                    visited[i][j] = 1
                    board[i][j] = '.'
                    start = (i, j)
                # 큐에 불과 상근이의 위치를 모두 저장해서 한번에 돌린다.
                elif board[i][j] == '*':
                    visited[i][j] = "FIRE"
                    q.append((i, j))
        
        # 상근이의 위치를 큐의 마지막에 저장해주기
        q.append(start)
        print(bfs())
                         