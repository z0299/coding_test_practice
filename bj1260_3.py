from collections import deque

n, m, v = map(int, input().split())
link = [list(map(int, input().split())) for _ in range(m)]
board = [[0]*(n+1) for _ in range(n+1)]
for i in range(m):
    board[link[i][0]][link[i][1]] = 1
    board[link[i][1]][link[i][0]] = 1
d_visited = [0]*(n+1)
b_visited = [0]*(n+1)
d_stack = [v]
b_stack = [v]

def dfs(v):
    print(d_stack)
    d_visited[v] = 1
    if len(d_stack) == n:
        print(' '.join(map(str, d_stack)))
        return
    for i in range(n+1):
        if board[v][i] == 1 and not d_visited[i]:
            d_visited[i] = 1
            d_stack.append(i)
            dfs(i)
            
def bfs():
    q = deque()
    q.append(v)
    b_visited[v] = 1
    while q:
        if len(b_stack) == n:
            print(' '.join(map(str, b_stack)))
            break
        x = q.popleft()
        for i in range(n+1):
            if board[x][i] == 1 and not b_visited[i]:
                b_visited[i] = 1
                b_stack.append(i)
                q.append(i)

dfs(v)
bfs()