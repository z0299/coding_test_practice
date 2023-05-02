import sys 
sys.setrecursionlimit(10**5)    # recursion Error가 난 문제!! recursion limit 강제로 늘려주기!

n, m = map(int, input().split())
ice = []
for i in range(n):
    ice.append(list(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
year = 0
delete_ice = [[0]*m for _ in range(n)]
ices = 0

def dfs(ice, visited, x, y):
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if ice[nx][ny] and not visited[nx][ny]:
            dfs(ice, visited, nx, ny)
    return visited

while ices < 2:
    # 얼음이 다 사라지면 while문 빠져 나가기
    flag = 0
    for i in range(n):
        if any(ice[i]):
            flag = 1
    if flag == 0:
        break
    
    year += 1
    # 사라질 얼음 갯수 구하기
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ice[i][j]:
                del_ice = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if ice[nx][ny] == 0:
                        del_ice -= 1
                delete_ice[i][j] = del_ice

    # 기존 얼음에 사라질 얼음 값 더하기
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ice[i][j]+delete_ice[i][j] < 0:
                ice[i][j] = 0
            else:
                ice[i][j] += delete_ice[i][j]
    
    # 얼음 덩이 개수 구하기
    visited = [[0]*m for _ in range(n)]
    temp = 0
    for i in range(1, n-1):
        for j in range(1, m-1):
            if ice[i][j] and not visited[i][j]:
                visited = dfs(ice, visited, i, j)
                temp += 1
    ices = temp
    
if ices < 2:
    print(0)
else:
    print(year)