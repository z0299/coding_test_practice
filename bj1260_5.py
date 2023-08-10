from collections import deque

n, m, v = map(int, input().split())
graph = {}
done = {i for i in range(1, n+1)}
# print(done)

for i in range(1, n+1):
    graph[i] = []

for i in range(m):
    x1, x2 = map(int, input().split())
    graph[x1].append(x2)
    graph[x2].append(x1)
    
for i in range(1, n+1):
    graph[i].sort()
# print(graph)
visited = set()

dfs_string = ""
def dfs(visited, node):
    global dfs_string
    
    visited.add(node)
    dfs_string += str(node)
    dfs_string += " "
    
    if visited == done:
        return
    
    for i in graph[node]:
        if i not in visited:
            dfs(visited, i)

q = deque()
visited_bfs = set()
bfs_string = ""
def bfs():
    global bfs_string
    
    while q:
        node = q.popleft()
        visited_bfs.add(node)
        bfs_string += str(node)
        bfs_string += " "
        for i in graph[node]:
            if i not in visited_bfs and i not in q:
                q.append(i)
    
dfs(visited, v)
print(dfs_string)

q.append(v)
bfs()
print(bfs_string)