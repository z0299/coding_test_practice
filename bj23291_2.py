from collections import deque
n, k = map(int, input().split())
board = []
board.append(deque(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def plus_one(board):
    for i in range(len(board[0])):
        if board[0][i] == min(board[0]):
            board[0][i] += 1
    return board

def left_to_up(board):
    temp_deque = deque()
    temp_deque.append(board[0][0])
    board[0].popleft()
    board.append(temp_deque)
    return board

def fly_board(board):
    while True:
        if len(board) > (len(board[0]) - len(board[-1])):
            break
        temp_list = []
        row = len(board)
        col = len(board[-1])
        
        for i in range(col):
            temp_deque = deque()
            for j in range(row):
                temp_deque.append(board[j].popleft())
            temp_list.append(temp_deque)
        
        board = [board[0]]
        # 90도 회전
        #temp_list = [deque([3, 3]), deque([14, 5])]
        for i in range(len(temp_list)-1, -1, -1):
            board.append(temp_list[i])
            
    return board
    
def change_fish(board):
    dif_map = [[0]*len(board[x]) for x in range(len(board))]
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0<=nx<len(board) and 0<=ny<len(board[nx]):
                    if board[x][y] > board[nx][ny]:
                        d = (board[x][y] - board[nx][ny]) // 5
                        if d >= 1:
                            dif_map[x][y] -= d
                    else:
                        d = (board[nx][ny] - board[x][y]) // 5
                        if d >= 1:
                            dif_map[x][y] += d
    #                 if (board[x][y] - board[nx][ny])//5 > 0:
    #                     print(x,y, board[x][y])
    #                     print(nx, ny, board[nx][ny])
    #                     print((board[x][y] - board[nx][ny])//5)
    #                     print("00000000000000")
    #                     dif_map[x][y] -= (board[x][y] - board[nx][ny])//5
    #                 elif (board[nx][ny] - board[x][y])//5 > 0 :
    #                     print(x,y, board[x][y])
    #                     print(nx, ny, board[nx][ny])
    #                     print((board[nx][ny] - board[x][y])//5)
    #                     print("11111111111111")
    #                     dif_map[x][y] += (board[x][y] - board[nx][ny])//5
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += dif_map[i][j]
    return board

def to_row(board):
    
    total_deque = deque()
    for i in range(len(board[-1])):
        temp_deque = deque()
        for j in range(len(board)):
            temp_deque.append(board[j][i])
        total_deque += temp_deque

    if len(board[0]) - len(board[-1]) > 0:
        for i in range(len(board[0]) - len(board[-1]), len(board[0])):
            total_deque.append(board[0][i])

    return [total_deque]

def rotate_180(the_list):
    temp_list = []
    
    for i in range(len(the_list)):
        the_list[i].reverse()
        temp_list.append(the_list[i])
    return temp_list

def fly_board2(board):
    first = []
    second = []
    
    # 첫번째 회전
    temp_deque = deque()
    for _ in range(n//2):
        temp_deque.append(board[0].popleft())
    first.append(temp_deque)
    
    # 180도 회전
    rotate_list = rotate_180(first)
    for i in range(len(rotate_list)):
        board.append(rotate_list[i])

    # 2번째 회전
    for i in range(2):
        temp_deque2 = deque()
        for j in range(n//4):
            temp_deque2.append(board[i].popleft())
        second.append(temp_deque2)
    
    rotate_list2 = rotate_180(second)
    for i in range(len(rotate_list2)-1, -1, -1):
        board.append(rotate_list2[i])
    return board
            

count = 0
while True:
    if max(board[0]) - min(board[0]) <= k:
        print(count)
        break
    #시행
    count += 1
    board = plus_one(board)
    board = left_to_up(board)
    board = fly_board(board)
    board = change_fish(board)
    board = to_row(board)
    board = fly_board2(board)
    board = change_fish(board)
    board = to_row(board)
