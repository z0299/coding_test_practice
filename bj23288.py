# ㅎㅎ; 얘도포기. 주사위 어떻게 처리해야하나?
n, m, k = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))
board.insert(0, [0]*m)
for i in range(n+1):
    board[i].insert(0, 0)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0
score = 0
x = 1
y = 1
bottom = 6
dice = [[6,[3,5,4,2]], [5,[3,1,4,6]], [4,[6,5,1,2]], [3,[1,5,6,2]], [2,[3,6,4,1]], [1,[4,5,3,2]]]



def other_side(dir):
    if dir == 1:
        return 3
    elif dir == 2:
        return 4
    elif dir == 3:
        return 1
    else:
        return 2
    
def get_up(t, dir):
    for i in range(len(dice)):
        if dice[i][0] == t:
            return dice[i][1][dir]
    
def move_dice(dir, x, y, top):
    nx = x + dx[dir]
    ny = y + dy[dir]
    if 0 < nx <= n and 0 < ny <= m:
        x = nx
        y = ny
        print(top)
        top = get_up(top, dir)
    else:
        dir = other_side(dir)
        x += dx[dir]
        y += dy[dir]
        top = get_up(top, dir)

    return dir, x, y, top

def dfs(x, y, visited, b):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<nx<=n and 0<ny<=m and board[nx][ny] == b and not visited[nx][ny]:
            visited[nx][ny] = visited[x][y] + 1
            dfs(nx, ny, visited, b)


def get_score():
    b = board[x][y]
    visited = [[0]*(m+1) for _ in range(n+1)]
    visited[x][y] += 1
    dfs(x, y, visited, b)
    c = 0
    for i in range(len(visited)):
        for j in range(len(visited[i])):
            if visited[i][j]:
                c += 1
    return b*(c)

def get_bottom(top):
    if top == 1:
        return 6
    elif top == 2:
        return 5
    elif top == 3:
        return 4
    elif top == 4:
        return 3
    elif top == 5:
        return 2
    else:
        return 1
    
def get_dir(bottom, x, y, dir):
    a = bottom
    b = board[x][y]
    if a > b:
        if dir == 3:
            dir = 0
        else:
            dir += 1
    elif a < b:
        if dir == 0:
            dir = 3
        else:
            dir -= 1
    else:
        pass
    return dir
    

count = 0
while True:
    if count == k:
        print(score)
        break
    
    count += 1
    dir, x, y, bottom = move_dice(dir, x, y, bottom)
    score += get_score()
    dir = get_dir(bottom, x, y, dir)
    print(x, y, dir, bottom, score)
    print("-------------------------------------")
