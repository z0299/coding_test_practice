# 시간초과나는 방식

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited_letter = []
max_num = 0

def dfs(x, y, cnt):
    global max_num
    max_num = max(cnt, max_num)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] not in visited_letter:
            visited_letter.append(board[nx][ny])
            dfs(nx, ny, cnt+1)
            visited_letter.pop()
    
visited_letter.append(board[0][0])
dfs(0, 0, 1)
print(max_num)
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
visited_letter = set()
max_num = 0

def dfs(x, y, cnt):
    global max_num
    max_num = max(cnt, max_num)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] not in visited_letter:
            visited_letter.add(board[nx][ny])
            dfs(nx, ny, cnt+1)
            visited_letter.remove(board[nx][ny])
    
visited_letter.add(board[0][0])
dfs(0, 0, 1)
print(max_num)
"""