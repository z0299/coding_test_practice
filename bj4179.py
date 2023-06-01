# 7:30~
"""
- 불의 개수는 1개 이상일 수 있다.
- 지훈이가 있는 곳은 다시 .으로 바꿔주기
- 1초가 지났을 때, 불을 먼저 퍼트리고 지훈이를 BFS하여 출구로 갈 수 있는지 확인
    - BFS가 아니고 DFS로 풀어야할 것 같다. 탈출 루트를 특정해야하기 때문.
    - DFS로도 풀리지 않는다. 로직이 잘못되었다. 매 초마다 지훈의 루트를 찾아 줄 수 없다. 왜냐하면 불이 다음번에 어떻게 번질지 예상해야하기 때문이다.
- 불이 퍼질 때 별도의 메모리를 만들어 퍼뜨려야 한다. (안그러면 1초가 되는 순간에 생긴 불에 대해 퍼질 수 있다)

- 새 로직은 다음과 같다.
  불을 먼저 다 번지게 한다. 이때 maze에 몇초에 번지는지 적는다. 
  그다음 지훈이를 bfs하면서, 지훈이가 도는 초에 해당 자리에 불이 있는지 없는지 판별한다.
  
- 빠뜨린 예외사항: 불이 안들어오는 경우..
"""
"""
from collections import deque
r,c = map(int, input().split())
maze = [list(input()) for _ in range(r)]
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(jh):
    q = deque()
    q.append(jh)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r-1 and 0<=ny<c-1 and maze[nx][ny] == '.' and not visited[]

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            jh = [i, j]
            maze[i][j] = '.'

while True:
    # 지훈이가 나갈 수 있는 경우
    if jh[0] == r-1 or jh[0] == 0 or jh[1] == c-1 or jh[1] == 0:
        print(answer+1)
        break

    # 1초가 지나고 불이 퍼진다
    answer += 1
    new_fire = []
    for x in range(r):
        for y in range(c):
            if maze[x][y] == 'F':
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0<=nx<r-1 and 0<=ny<c-1 and maze[nx][ny] == '.':
                        new_fire.append([nx, ny])
                        
    for fire in new_fire:
        maze[fire[0]][fire[1]] = 'F'
    
    # 지훈이가 나갈 수 있는지 확인
    bfs(jh)
"""
from collections import deque
from copy import deepcopy
r,c = map(int, input().split())
maze = [list(input()) for _ in range(r)]
answer = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
fire_list = []

def fire_bfs(fire_list):
    q = deque()
    visited_fire = deepcopy(maze)
    for fire in fire_list:
        visited_fire[fire[0]][fire[1]] = 0
        q.append(fire)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and visited_fire[nx][ny] != '#' and type(visited_fire[nx][ny]) is not int :
                visited_fire[nx][ny] = visited_fire[x][y] + 1
                q.append([nx, ny])
    return visited_fire

def jh_bfs(jh, fire_maze):
    q = deque()
    q.append(jh)
    visited_jh = deepcopy(maze)
    visited_jh[jh[0]][jh[1]] = 0
    while q:
        x, y = q.popleft()
        if x == r-1 or y == c-1 or x == 0 or y == 0:
            print(visited_jh[x][y] + 1)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and visited_jh[nx][ny] != '#' and type(visited_jh[nx][ny]) is not int: 
                if fire_maze[nx][ny] == '.':
                    visited_jh[nx][ny] = visited_jh[x][y] + 1
                    q.append([nx, ny])
                elif type(fire_maze[nx][ny]) is int and (visited_jh[x][y]+1) < fire_maze[nx][ny]:
                    visited_jh[nx][ny] = visited_jh[x][y] + 1
                    q.append([nx, ny])
    print("IMPOSSIBLE")

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            jh = [i, j]
            maze[i][j] = '.'
        if maze[i][j] == 'F':
            fire_list.append([i, j])
            maze[i][j] = '.'

fire_maze = fire_bfs(fire_list)
jh_bfs(jh, fire_maze)