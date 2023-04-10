#포기.. 못풀겠다 도저히..
import copy
m, s = map(int, input().split())
fish_list = []
for i in range(m):
    fish_list.append(list(map(int, input().split())))
sx, sy = map(int, input().split())

f_dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
s_dx = [0, -1, 0, 1, 0]
s_dy = [0, 0, -1, 0, 1]
board = [[0]*5 for _ in range(5)]
smell_board = [[0]*5 for _ in range(5)]

def copy_fish(fish_list):
    copy_list = copy.deepcopy(fish_list)
    return copy_list
    
def move_fish(board, fish_list, smell_board):
    for i in range(len(fish_list)):
        x = fish_list[i][0]
        y = fish_list[i][1]
        vector = fish_list[i][2]
        
        for _ in range(8):
            nx = x + f_dx[vector]
            ny = y + f_dy[vector]
            if (1<=nx<5 and 1<=ny<5) and (nx != sx or ny != sy) and not(smell_board[nx][ny]):
                fish_list[i][0] = nx
                fish_list[i][1] = ny
                fish_list[i][2] = vector
            else:
                if vector == 1:
                    vector = 8
                else:
                    vector -= 1
                continue
            
    #board = [[0]*5 for _ in range(5)]
    for i in range(len(fish_list)):
        board[fish_list[i][0]][fish_list[i][1]] += 1
        
    return fish_list, board
    
def shark_move(board, sx, sy, smell_board):
    eat_fish_count = [0]*64
    move_list = []
    for a in range(1,5):
        for b in range(1, 5):
            for c in range(1, 5):
                move_list.append([a, b, c])
    print(board)
    for i in range(len(move_list)):
        count = 0
        for j in range(3):
            nx = sx + s_dx[move_list[i][j]]
            ny = sy + s_dy[move_list[i][j]]
            if 0<nx<=4 and 0<ny<=4:
                print(i, count)
                count += board[nx][ny]
        eat_fish_count[i] = count

    move_index = eat_fish_count.index(max(eat_fish_count))
    # for i in range(64):
    #     if eat_fish_count[i] == max(eat_fish_count):
    #         print(move_list[i])
    # print(eat_fish_count)
    # #print(move_list)
    # print(len(eat_fish_count))
    # print(len(move_list))
    # print(move_list[move_index])
    for i in range(3):
        sx += s_dx[move_list[move_index][i]]
        sy += s_dy[move_list[move_index][i]]
        if board[sx][sy]:
            board[sx][sy] = 0
            smell_board[sx][sy] += 1
            for j in range(len(fish_list)):
                if sx == fish_list[j][0] and sy == fish_list[j][1]:
                    fish_list.remove(fish_list[j])
                    break

    return sx, sy, smell_board, fish_list

def smell_destroy(smell_board):
    for i in range(5):
        for j in range(5):
            if smell_board[i][j]:
                if smell_board[i][j] == 3:
                    smell_board[i][j] = 0
    return smell_board     

def copy_magic(fish_list, board, copy_list):
    for i in range(len(copy_list)):
        fish_list.append(copy_list[i])
        board[copy_list[i][0]][copy_list[i][1]] += 1
    return fish_list, board

count = 0
while True:
    if count == s:
        fish_count = 0
        for i in range(len(board)):
            fish_count += board[i].count(True)
        print(fish_count)
        break

    count += 1
    # 행동
    copy_list = copy_fish(fish_list)
    fish_list, board = move_fish(board, fish_list, smell_board)
    sx, sy, smell_board, fish_list = shark_move(board, sx, sy, smell_board)
    smell_board = smell_destroy(smell_board)
    fish_list, board = copy_magic(fish_list, board, copy_list)
    print(board)


# print(smell_board)
# print(board)
# print(fish_list)
# print(sx, sy)