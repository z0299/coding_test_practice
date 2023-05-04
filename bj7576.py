#날짜 세주는 완탐은 앞에거 +1 해가면서 하자..!
import sys
sys.setrecursionlimit(10**5)

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]
day = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 모든 토마토가 익은 상태인지, 모두 익지 못하는 상황인지 확인
def all_tomato():
    all_tomato = 1
    for x in range(n):
        for y in range(m):
            if tomato[x][y] == 0:
                all_tomato = 0
                flag = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] != -1:
                        flag = 1 
                if flag == 0:   # 모두 익지 못하는 경우
                    print(-1)
                    exit()
    if all_tomato == 1:     # 모두 익어있는 경우
        print(day)
        exit()
    
# def bfs(x, y):
#     q = deque()
#     q.append([x, y])
#     visited = [[0]*m for _ in range(n)]
#     visited[x][y] = 1
    
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0 and not visited[nx][ny]:
#                 visited[nx][ny] = 1
#                 tomato[nx][ny] = 1
#                 q.append([nx, ny])

all_tomato()

# 토마토 익히기
visited_tomato = [[0]*m for _ in range(n)]
while True:
    #all_tomato()
    all_tomato2 = 1
    for x in range(n):
        for y in range(m):
            if tomato[x][y] == 0:
                all_tomato2 = 0
    if all_tomato2 == 1:
        print(day)
        exit()
    
    day += 1
    visited = [[0]*m for _ in range(n)]

    def dfs(x, y):
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0 and not visited[nx][ny]:
                tomato[nx][ny] = 1
                visited[nx][ny] = 1
            elif 0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 1 and not visited[nx][ny]:
                dfs(nx, ny)
           
    for x in range(n):
        for y in range(m):
            if tomato[x][y] == 1 and not visited_tomato[x][y] and not visited[x][y]:
                visited_tomato[x][y] = 1
                dfs(x, y)
                print(tomato)
