# dfs 알고리즘 공부 - 20분

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(ice, visited, x, y):
    visited[x][y] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<4 and 0<=ny<5 and not visited[nx][ny] and ice[nx][ny] == 0:
            dfs(ice, visited, nx, ny)
        
if __name__=="__main__":
    n, m = map(int, input().split())
    ice = []
    count = 0
    for i in range(n):
        ice.append(list(map(int, input())))
    visited = [[0]*(m) for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if ice[i][j] == 0 and not visited[i][j]:
                count += 1
                dfs(ice, visited, i, j)
    print(count)