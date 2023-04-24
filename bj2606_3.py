n = int(input())
nw = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(nw):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
    
def dfs(x, visited):
    visited[x] = 1
    
    for i in range(1, n+1):
        if graph[x][i] == 1 and not visited[i]:
            dfs(i, visited)
    return visited

visited = [0]*(n+1)
visited = dfs(1, visited)
print(visited.count(1)-1)