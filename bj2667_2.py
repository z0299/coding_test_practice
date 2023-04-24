n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(visited, x, y, ll):
    visited[x][y] = 1
    graph[x][y] = -1
    ll.append([x, y])
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and graph[nx][ny] == 1:
            dfs(visited, nx, ny, ll)
    
    return graph, ll

count = 0
visited = [[0]*n for _ in range(n)]
ll_list = []
for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            count += 1
            lenlist = []
            graph, lenlist = dfs(visited, x, y, lenlist)
            ll_list.append(len(lenlist))

ll_list.sort()
print(count)
for i in range(count):
    print(ll_list[i])
            