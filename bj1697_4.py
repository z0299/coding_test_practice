from collections import deque

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v, dfs_list):
    dfs_list.append(v)
    for i in range(1, n+1):
        if graph[v][i] == 1 and i not in dfs_list:
            dfs(i, dfs_list)
    return dfs_list

def bfs(v, bfs_list):
    q = deque()
    q.append(v)
    bfs_list.append(v)
    
    while q:
        x = q.popleft()
        for i in range(1, n+1):
            if graph[x][i] == 1 and i not in bfs_list:
                q.append(i)
                bfs_list.append(i)
    return bfs_list
    
dfs_list = []
bfs_list = []
dfs_list = dfs(v, dfs_list)
bfs_list = bfs(v, bfs_list)
print(' '.join(map(str, dfs_list)))
print(' '.join(map(str, bfs_list)))