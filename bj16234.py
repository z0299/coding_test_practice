import copy

n, l, r = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
count = 0
d = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def dfs(x, y):
    union[(x, y)] = board[x][y]
    visited[x][y] = 1
    for i in range(4):
        nx = x + d[i][0]
        ny = y + d[i][1]
        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if l <= abs(board[x][y] - board[nx][ny]) <= r:
                dfs(nx, ny) 
    return

while True:
    count += 1
    temp_board = copy.deepcopy(board)
    visited = [[0]*n for _ in range(n)]
    
    for x in range(n):
        for y in range(n):
            if not visited[x][y]:
                union = {}
                dfs(x, y)
                
                # 연합이 없으면 다음 연합 찾기
                if len(union) == 1:
                    continue
                
                # 연합이 있을때, 인구 수 구하기
                num = 0              
                for i in union:
                    num += union[i]
                num = num // len(union)

                # 인구 이동하기
                for key in union:
                    board[key[0]][key[1]] = num
    
    # 인구 변화가 없는 경우(연합이 없는 경우) 종료      
    if board == temp_board:
        break
    
print(count-1)