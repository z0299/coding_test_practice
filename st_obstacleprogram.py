import sys

def dfs(cnt, x, y):
  visited[x][y] = 1
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 1 and not visited[nx][ny]:
      cnt = dfs(cnt+1, nx, ny)
  return cnt

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
answer = []
visited = [[0]*n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
  for j in range(n):
    if board[i][j] == 1 and not visited[i][j]:
      cnt = dfs(1, i, j)
      answer.append(cnt)

print(len(answer))
answer.sort()
for i in answer:
  print(i)