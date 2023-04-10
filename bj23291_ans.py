# 어항정리
from collections import deque
n, k = map(int, input().split())
#direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []
board.append(deque(list(map(int, input().split()))))

# 수가 가장 적은 어학에 +1마리
def push_fish_to_min_bowl(board):
    for i in range(len(board[0])):
        if board[0][i] == min(board[0]):
            board[0][i] += 1

# 젤 왼쪽 어항을 그 오른쪽 위에 쌓기
def left_to_up(board):
    pop = board[0].popleft()
    board.append(deque([pop]))
    #print(board)

# 공중에 뜬 어항 90도 회전하기
def rotate_90_clockwise(bowls):
    new_bowls = [[0]*len(bowls) for _ in range(len(bowls[0]))]
    for i in range(len(bowls[0])):
        for j in range(len(bowls)):
            new_bowls[i][j] = bowls[j][len(bowls[0])-1-i]
    return new_bowls
    
# 2층 이상의 어항들 분리해서 공중부양 시키기
def fly_blocks(board):
    while True:
        if len(board) > len(board[0]) - len(board[-1]):
            break
        
        will_fly_blocks = []
        will_fly_blocks_row = len(board)
        will_fly_blocks_col = len(board[-1])
        
        # n층 어항 분리
        for i in range(will_fly_blocks_row):
            new_deque = deque()
            for _ in range(will_fly_blocks_col):
                new_deque.append(board[i].popleft())
            will_fly_blocks.append(new_deque)
        
        # 분리하고 남은 어항
        board = [board[0]]
        
        # 분리한 (n층)어항 90도 회전
        rotated_blocks = rotate_90_clockwise(will_fly_blocks)
        
        # 90도 회전한 어항 쌓기
        for row in rotated_blocks:
            board.append(deque(row))
    
    return board

# 어항의 물고기 수 조절 
def fix_fish_num(board):
    # 물고기 수 조절이 동시에 일어나기 때문에 다음의 그래프가 필요
    dp = [[0]*len(board[x]) for x in range(len(board))]

    for x in range(len(board)):
        for y in range(len(board[x])):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0<=nx<len(board) and 0<=ny<len(board[nx]):
                    # 현재 칸이 인접 칸보다 크다면
                    #print(nx, ny)
                    if board[x][y] > board[nx][ny]:
                        c = (board[x][y] - board[nx][ny]) // 5
                        if c > 0:
                            dp[x][y] -= c
                    # 현재 칸이 인접 칸보다 작다면
                    else:
                        c = (board[nx][ny] - board[x][y]) // 5
                        if c > 0:
                            dp[x][y] += c
                            
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] += dp[i][j]

# 어항 다시 일렬로 두기            
def put_bowl_in_a_row(board):
    new_deque = deque()
    
    # n층짜리 어항부터 일렬로 정렬 후 합친다
    for i in range(len(board[-1])):
        for j in range(len(board)):
            new_deque.append(board[j][i])
    # 나머지 어항 합치기
    for i in range(len(board[-1]), len(board[0])):
        new_deque.append(board[0][i])
        
    result_list = []
    result_list.append(new_deque)
    return result_list

# 180도 회전
def rotate_180_clockwise(graph):
    new_graph = []
    for i in reversed(range(len(graph))):
        graph[i].reverse()
        new_graph.append(graph[i])
    return new_graph

# 2번 절반 자르기   
def fly_blocks2(board):
    left1 = []
    left2 = []
    new_deque = deque()
    for _ in range(n//2):
        new_deque.append(board[0].popleft())
    # deque reverse는 적용만되고 return은 아무것도 하지 않는다.
    # new_deque.reverse()
    # temp_list = []
    # temp_list.append(new_deque)
    left1.append(new_deque)
    rotated_left1 = rotate_90_clockwise(left1)

    board += rotated_left1

    # 두 번째 절반 자르기
    for i in range(2):
        temp_deque = deque()
        for _ in range(n//4):
            temp_deque.append(board[i].popleft())
        left2.append(temp_deque)
    rotated_left2 = rotate_180_clockwise(left2)
    board += rotated_left2
        

def get_result(board):
    dq = board[0]
    result = max(dq) - min(dq)
    return result
    
answer = 0
while True:
    result = get_result(board)
    if result <= k:
        print(answer)
        break
    push_fish_to_min_bowl(board)
    print(board)
    left_to_up(board)
    print(board)
    board = fly_blocks(board)
    print(board)
    fix_fish_num(board)
    print(board)
    board = put_bowl_in_a_row(board)
    print(board)
    fly_blocks2(board)
    print(board)
    fix_fish_num(board)
    print(board)
    board = put_bowl_in_a_row(board)
    print(board)
    answer += 1
    print("------------------------------")

