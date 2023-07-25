"""
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# 비율 배열 만들기
p = []
left = [[0, 0, 0.02, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0.05, 0, 0, 0, 0],
        [0, 0.1, 0.07, 0.01, 0],
        [0, 0, 0.02, 0, 0]]

def rotate_90(arr):
    temp = list(map(list, zip(*arr)))[::-1]
    return temp

p.append(left)
for i in range(3):
    temp = rotate_90(p[i])
    p.append(temp)

outer_sand = 0
t_x = n//2
t_y = n//2
move = 1
direction = -1

#while not(t_x == 0 and t_y == 0):
for _ in range(4):
    move += 1
    direction = (direction+1)%4
    move_board = p[direction]
    temp = [[0]*5 for _ in range(5)]
    print(direction, move//2)
    
    if direction == 0:
        t_y -= 1
        val = board[t_x][t_y]
        for x in range(5):
            for y in range(5):
                if move_board[x][y] != 0:
                    nx = t_x + x-2
                    ny = t_y + y-2
                    if 0 <= nx < n and 0 <= ny < y:
                        board[nx][ny] += int(val*move_board[x][y])
                    else:
                        outer_sand += int(val*move_board[x][y])
                board[t_x][t_y] -= int(val*move_board[x][y])
        if 0 <= t_y - 1 < n:
            board[t_x][t_y-1] += board[t_x][t_y]
        else:
            outer_sand += board[t_x][t_y]
        board[t_x][t_y] = 0
    
    elif direction == 1:
        t_x += 1
        val = board[t_x][t_y]
        for x in range(5):
            for y in range(5):
                if move_board[x][y] != 0:
                    nx = t_x + x-2
                    ny = t_y + y-2
                    if 0 <= nx < n and 0 <= ny < y:
                        board[nx][ny] += int(val*move_board[x][y])
                    else:
                        outer_sand += int(val*move_board[x][y])
                board[t_x][t_y] -= int(val*move_board[x][y])
        if 0 <= t_x + 1 < n:
            board[t_x+1][t_y] += board[t_x][t_y]
        else:
            outer_sand += board[t_x][t_y]
        board[t_x][t_y] = 0
    
    elif direction == 2:
        t_y += 1
        val = board[t_x][t_y]
        for x in range(5):
            for y in range(5):
                if move_board[x][y] != 0:
                    nx = t_x + x-2
                    ny = t_y + y-2
                    if 0 <= nx < n and 0 <= ny < y:
                        board[nx][ny] += int(val*move_board[x][y])
                    else:
                        outer_sand += int(val*move_board[x][y])
                board[t_x][t_y] -= int(val*move_board[x][y])
        if 0 <= t_y + 1 < n:
            board[t_x][t_y+1] += board[t_x][t_y]
        else:
            outer_sand += board[t_x][t_y]
        board[t_x][t_y] = 0
    
    elif direction == 3:
        t_x -= 1
        val = board[t_x][t_y]
        for x in range(5):
            for y in range(5):
                if move_board[x][y] != 0:
                    nx = t_x + x-2
                    ny = t_y + y-2
                    if 0 <= nx < n and 0 <= ny < y:
                        board[nx][ny] += int(val*move_board[x][y])
                    else:
                        outer_sand += int(val*move_board[x][y])
                board[t_x][t_y] -= int(val*move_board[x][y])
        if 0 <= t_x - 1 < n:
            board[t_x-1][t_y] += board[t_x][t_y]
        else:
            outer_sand += board[t_x][t_y]
        board[t_x][t_y] = 0
    
    print(board, outer_sand)
"""

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
tx = ty = int(n/2)

# 토네이도 방향별 비율 배열 생성
def rotate_90(proportion):
    new_proportion = list(map(list, zip(*proportion)))[::-1]
    return new_proportion
p_left = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], 
        [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], 
        [0, 0, 0.02, 0, 0]]
p_down = rotate_90(p_left)
p_right = rotate_90(p_down)
p_up = rotate_90(p_right)
p = [p_left, p_down, p_right, p_up]
alphas = [(2, 1), (3, 2), (2, 3), (1, 2)]

# 토네이도 이동 방향
dir = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# 초기 세팅
outer_sand = 0
direction = 0
turn = 2
tornado_length = 0
proportion = p[0]

while not(tx == 0 and ty == 0):
    tx += dir[direction][0]
    ty += dir[direction][1]
    tornado_length += 1
    sand = board[tx][ty]
    board[tx][ty] = 0
    left = sand
    
    # 모래 이동
    for x in range(5):
        for y in range(5):
            now_sand = int(sand*proportion[x][y])
            left -= now_sand
            if 0 <= tx+x-2 < n and 0 <= ty+y-2 < n:
                board[tx+x-2][ty+y-2] += now_sand
            else:
                outer_sand += now_sand
                
    # 남은 모래
    if 0 <= tx+alphas[direction][0]-2 < n and 0 <= ty+alphas[direction][1]-2 < n:
        board[tx+alphas[direction][0]-2][ty+alphas[direction][1]-2] += left
    else:
        outer_sand += left
        
    # 토네이도 방향 바꾸기
    if tornado_length == turn // 2 or tornado_length == turn:
        direction = (direction+1)%4
        proportion = p[direction]
        if tornado_length == turn:
            tornado_length = 0
            turn += 2
            
print(outer_sand)