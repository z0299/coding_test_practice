"""
n = int(input())
answer = 0

board = []
def dfs(x, idx):
    global answer
    
    # n개 다 놓으면 방법 수 더하기
    if len(board) == n:
        answer += 1
    
    # n개가 아니면
    for y in range(idx, n):
        # flag = 0
        
        # 상하, 좌우, 대각선 확인
        for i in range(len(board)):
            print(board[i][0], board[i][1], x, y)
            if board[i][0] == x or board[i][1] == y or abs(board[i][0] - x) == abs(board[i][1] - y):
                return
            
        # 퀸을 둘 수 있는 경우   
        # if flag == 0:
        board.append((x, y))
        print(board)
        if y == n-1:
            dfs(x+1, y+1)
            board.pop()
        else:
            dfs(x, y+1)
            board.pop()
        # 퀸을 둘 수 없는 경우
        # else:
        #     if y == n-1:
        #         dfs(x+1, y+1)
        #     else:
        #         dfs(x, y+1)
    # board.pop()
    return

dfs(0, 0)
print(answer)
"""
n = int(input())
answer = 0
row = [0]*n

def is_promising(x):
    for i in range(x):
        if row[i] == row[x] or abs(x-i) == abs(row[x]-row[i]):
            return False
    return True

def dfs(x):
    global answer
    
    if x == n:
        answer += 1
        return
    
    for i in range(n):
        row[x] = i
        if is_promising(x):
            dfs(x+1)

dfs(0)
print(answer)