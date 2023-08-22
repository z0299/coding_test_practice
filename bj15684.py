# 9:10 ~
# 4:00 ~
"""
n, m, h = map(int, input().split())
board = [[0]*(n+1) for _ in range(h+1)]

def check():
    for l in range(1, n+1):
        line = l
        for row in range(1, h+1):
            if board[row][line] == 1:
                line += 1
            elif board[row][line-1] == 1:
                line -= 1

        if l != line:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if check():
        print(board)
        ans = min(cnt, ans)
        return
    elif cnt == 3 or ans <= cnt:
        print(board)
        return
        
    for row in range(x, h):
        if row == x:
            now = y
        else:
            now = 1
            
        for line in range(now, n):
            if board[row][line] == 0 and board[row][line+1] == 0:
                if line > 0 and board[row][line-1] == 1:
                    continue
                board[row][line] = 1
                dfs(cnt+1, row, line+2)
                board[row][line] = 0

for _ in range(m):
    x, y = map(int, input().split())
    board[x][y] = 1
# print(board)

ans = 4
dfs(0, 1, 1)
print(ans if ans < 4 else -1)
"""

def check():
    for start in range(n):
        now = start
        for j in range(h):
            if board[j][now]:
                now += 1
            elif now > 0 and board[j][now-1]:
                now -= 1
        if now != start:
            return False
    return True

def dfs(cnt, x, y):
    global ans
    if check():
        ans = min(ans, cnt)
        return
    elif cnt == 3 or ans <= cnt:
        return
    
    for i in range(x, h):
        if i == x:
            now = y
        else:
            now = 0
            
        for j in range(now, n-1):
            if board[i][j] == 0 and board[i][j+1] == 0:
                if j > 0 and board[i][j-1]:
                    continue
                board[i][j] = True
                dfs(cnt+1, i, j+2)
                board[i][j] = False

n, m, h = map(int, input().split())
board = [[0]*n for _ in range(h)]

for _ in range(m):
    x, y = map(int, input().split())
    board[x-1][y-1] = 1
    
ans = 4
dfs(0, 0, 0)
print(ans if ans < 4 else -1)