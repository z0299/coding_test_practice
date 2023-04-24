def rotate_90(dol):
    new_dol = []
    for i in range(len(dol)):
        new_dol.append([dol[i][1], len(dol)-dol[i][0]-1])
    return new_dol

def to_00(board):
    row = int(1e9)
    col = int(1e9)
    new_board = [[0,0] for _ in range(len(board))]
    for i in range(len(board)):
        row = min(row, board[i][0])
        col = min(col, board[i][1])
    for i in range(len(board)):
        new_board[i][0] = board[i][0]-row
        new_board[i][1] = board[i][1]-col
    return new_board

def solution(key, lock):
    k_n = len(key)
    l_n = len(lock)
    
    not_home = []
    home = []
    for i in range(l_n):
        for j in range(l_n):
            if lock[i][j] == 0:
                home.append([i, j])
            if lock[i][j] == 1:
                not_home.append([i, j])
    
    dol = []
    for i in range(k_n):
        for j in range(k_n):
            if key[i][j] == 1:
                dol.append([i, j])

    # print(not_home)
    home = to_00(home)
    print(not_home)
    for i in range(4):
        dol = rotate_90(dol)
        dol = to_00(dol)
        print(dol)
        f = 1
        
        # 돌과 돌이 부딪히는지 확인
        for d in range(len(dol)):
            #print(dol[d])
            if dol[d] in not_home:
                f = 0
                break
        
        # 홈이 돌에 맞는지 확인
        for j in range(len(home)):
            if home[j] not in dol:
                f = 0
                break
        if f == 1:
            # print(home)
            # print(dol)
            return True
    return False
        
    # print(home)
    # print(dol)
    # new_dol = rotate_90(dol)
    # print(new_dol)

    #return answer