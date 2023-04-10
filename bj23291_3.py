# 첫번째 단계인 최소 물고기를가지는 어항에 +1을 해줄때, 조건문에 바로 min(graph)를 넣으면, 
# for문을 돌 때마다 min(graph)값이 바뀌어버리게 되서 틀렸었다... 따로 선언을 해주고 실행해줘야한다!
from collections import deque
n, k = map(int, input().split())
board = []
board.append(deque(map(int, input().split())))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def plus_one(graph):
    min_fish = min(graph)
    for i in range(n):
        if graph[i] == min_fish:
        # if graph[i] == min(graph): 를 해서 틀렸었다!!
            graph[i] += 1

def left_to_top(board):
    temp_q = deque([board[0].popleft()])
    board.append(temp_q)
    
# def rotate_90(floor, temp):
#     new_board = []
#     new_board.append(floor)
#     for _ in range(len(temp)):
#         new_board.append(temp.pop())
#     return new_board
    
# def fishbowl_fly(board):
#     while (len(board[0])-len(board[-1])) >=  len(board):
#         temp_board = []
#         row = len(board)
#         col = len(board[-1])
        
#         for i in range(col):
#             temp_q = deque()
#             for j in range(row):
#                 temp_q.append(board[j].popleft())
#             temp_board.append(temp_q)
#         board = rotate_90(board[0], temp_board)
        
#     return board

# 공중에 뜬 어항들을 시계방향 90도 회전하기
def rotate_90_clockwise(bowls):
    new_bowls = [[0] * len(bowls) for _ in range(len(bowls[0]))]
    for i in range(len(bowls[0])):
        for j in range(len(bowls)):
            new_bowls[i][j] = bowls[j][len(bowls[0])-1-i]

    return new_bowls


# 2개 이상 쌓인 어항들을 분리해서 공중부양 시키기
def fly_blocks(graph):
    while True:
        if len(graph) > len(graph[0]) - len(graph[-1]):
            break

        will_fly_blocks = []
        will_fly_blocks_row = len(graph)
        will_fly_blocks_col = len(graph[-1])

        for i in range(will_fly_blocks_row):
            new_deque = deque()
            for _ in range(will_fly_blocks_col):
                new_deque.append(graph[i].popleft())
            will_fly_blocks.append(new_deque)

        graph = [graph[0]]
        rotated_blocks = rotate_90_clockwise(will_fly_blocks)
        for row in rotated_blocks:
            graph.append(deque(row))

    return graph

def fish_resize():
    change_board = []
    for i in range(len(board)):
        change_board.append(deque([0]*len(board[i])))
    
    for x in range(len(board)):
        for y in range(len(board[x])):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < len(board) and 0 <= ny < len(board[nx]):
                    if board[x][y] > board[nx][ny]:
                        d = (board[x][y] - board[nx][ny])//5
                        if d > 0:
                            change_board[x][y] -= d
                    elif board[x][y] < board[nx][ny]:
                        d = (board[nx][ny] - board[x][y])//5
                        if d > 0:
                            change_board[x][y] += d
    for x in range(len(board)):
        for y in range(len(board[x])):
            board[x][y] += change_board[x][y]
            
def to_row():
    new_board = []
    temp_q = deque()
    if len(board[0]) == len(board[-1]):
        for y in range(len(board[0])):
            for x in range(len(board)):
                temp_q.append(board[x][y])
        return [temp_q]
    else:            
        for _ in range(len(board[0]) - (len(board[-1]))):
            for i in range(len(board)):
                temp_q.append(board[i].popleft())
        new_board.append(temp_q)
        new_board[0] += board[0]
        return new_board

# def rotate_180(board, temp_list):
#     for i in range(len(temp_list)-1, -1, -1):
#         temp_list[i].reverse()
#         board.append(temp_list[i])
#     return board

# def fishbowl_fly2(board):
#     temp_q = deque()
#     temp_list = []
#     for i in range(len(board[0])//2):
#         temp_q.append(board[0].popleft())
#     temp_list.append(temp_q)
#     board = rotate_180(board, temp_list)
    
#     temp_list2 = []
#     for i in range(2):
#         temp_q2 = deque()
#         for j in range(len(board[i])//2):
#             temp_q2.append(board[i].popleft())
#         temp_list2.append(temp_q2)
#     board = rotate_180(board, temp_list2)
# 180 도 회전
def rotate_180_clockwise(graph):
    new_graph = []

    for i in reversed(range(len(graph))):
        graph[i].reverse()
        new_graph.append(graph[i])

    return new_graph


# 다시 공중부양 작업을 한다. 이번에는 절반을 자르는데 2번 수행한다.
def fly_blocks2(graph):
    left1 = list()
    left2 = list()
    new_deque1 = deque()
    for i in range(n//2):
        new_deque1.append(graph[0].popleft())
    left1.append(new_deque1)
    rotated_left1 = rotate_180_clockwise(left1)
    graph += rotated_left1

    for i in range(2):
        temp_deque = deque()
        for j in range(n//4):
            temp_deque.append(graph[i].popleft())
        left2.append(temp_deque)
    rotated_left2 = rotate_180_clockwise(left2)
    graph += rotated_left2
    
    return graph

count = 0
while True:
    if max(board[0]) - min(board[0]) <= k:
        print(count)
        break
    count += 1
    # 1
    plus_one(board[0])
    # 2
    left_to_top(board)
    # 3
    #board = fishbowl_fly(board)
    board = fly_blocks(board)
    # 4
    fish_resize()
    # 5
    board = to_row()

    # 6
    #fishbowl_fly2(board)
    board = fly_blocks2(board)

    # 7
    fish_resize()
    # 8
    board = to_row()
