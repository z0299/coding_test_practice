from collections import deque
q = deque()
n, k = map(int, input().split())
visited = [0]*(200)

def go(i, x):
    if i == 0:
        return x+1
    elif i == 1:
        return x-1
    elif i == 2:
        return 2*x

def bfs(x):
    global visited
    q.append(x)
    visited[x] = 1
    while q:
        x = q.popleft()
        if x == k:
            print(visited[k])
            return
        for i in range(3):
            nx = go(i, x)
            visited[nx] = visited[x] + 1
            q.append(nx)

            
bfs(n)
print(visited)