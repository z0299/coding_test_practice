# 3:00 ~
"""
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

cctv = {1:[], 2:[], 3:[], 4:[], 5:[]}

for i in range(n):
    for j in range(m):
        if board[i][j] != 0 and board[i][j] != 6:
            cctv[board[i][j]].append((i, j))
print(cctv)

def dfs(x, y, dir):
    x += dir[0]
    y += dir[1]
    if 0 <= x < n and 0 <= y < m and board[x][y] != 6:
        board[x][y] = -1
        dfs(x, y, dir)
    else:
        return

answer_board = []
while len(cctv[1])+len(cctv[2])+len(cctv[3])+len(cctv[4])+len(cctv[5]) != 0:
    # 5번 cctv
    for c in cctv[5]:
        x, y = c[0], c[1]
        dfs(x, y, dir[0])
        dfs(x, y, dir[1])
        dfs(x, y, dir[2])
        dfs(x, y, dir[3])
    cctv[5] = []
    
    temp_board = []
    for x in range(n):
        temp = []
        for y in range(m):
            temp.append(board[x][y])
        temp_board.append(temp)
    # print(temp_board)  
    
    # 2번 cctv
    for c in cctv[2]:
        x, y = c[0], c[1]
        for dirs in [[dir[1], dir[3]], [dir[0], dir[2]]]:
            temp_board = dfs(board, x, y, dirs[0])
            temp_board = dfs(temp_board, x, y, dirs[1])
            answer_board.append(temp_board)
            break
    break
    
    dirs = []
    # 나머지 cctv
    for i in range(1, 5):
        for j in cctv[i]:
    
    # 백트래킹
    for i in range(1, 5):
        for c in cctv[i]:
            dfs(c[0], c[1], )
print(answer_board)
"""
"""
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
dirs = {1: [(-1, 0), (0, 1), (1, 0), (0, -1)],
       2: [[(0, 1), (0, -1)], [(-1, 0), (1, 0)]],
       3: [[(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(0, -1), (-1, 0)]],
       4: [[(0, -1), (-1, 0), (0, 1)], [(-1, 0), (0, 1), (1, 0)], [(0, 1), (1, 0), (0, -1)], [(1, 0), (0, -1), (-1, 0)]],
       5: [[(-1, 0), (0, 1), (1, 0), (0, -1)]]}

def dfs(cctv, dir):
    if cctv

for i in range(n):
    for j in range(m):
        if board[i][j] != 6 and board[i][j] != 0 and board[i][j] != -1:
            dfs(board[i][j], dirs[board[i][j]])
"""

import copy
n, m = map(int, input().split())
cctv = []
board = []
mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[0, 1, 2], [0, 1, 3], [1, 2, 3], [0, 2, 3]],
    [[0, 1, 2, 3]]
]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    data = list(map(int, input().split()))
    board.append(data)
    for j in range(m):
        if data[j] in [1, 2, 3, 4, 5]:
            cctv.append([data[j], i, j])
            
def fill(board2, dir, x, y):
    for d in dir:
        nx = x
        ny = y
        while True:
            nx += dx[d]
            ny += dy[d]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                break
            if board2[nx][ny] == 6:
                break
            elif board2[nx][ny] == 0:
                board2[nx][ny] = 7

def dfs(depth, arr):
    global min_value
    
    if depth == len(cctv):
        count = 0
        for i in range(n):
            count += arr[i].count(0)
        min_value = min(min_value, count)
        return

    temp = copy.deepcopy(arr)
    cctv_num, x, y = cctv[depth]
    for dir in mode[cctv_num]:
        fill(temp, dir, x, y)
        dfs(depth+1, temp)
        temp = copy.deepcopy(arr)   # 백트래킹 - 원래의 배열로 되돌리기
       
min_value = int(1e9)
dfs(0, board)
print(min_value)