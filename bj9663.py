# n = int(input())
# dx = [1, -1, 1, -1]
# dy = [-1, 1, -1, 1]
# answer = 0
# board = [[0]*n for _ in range(n)]

# def check_cross(x, y, visited):
#     for d in range(4):
#         for i in range(n-1):
#             nx = x + dx[d]*i
#             ny = y + dy[d]*i
            
#             if 0<=nx<n and 0<=ny<n and board[nx][ny] == 1:
#                 return 1
#             else:
#                 continue
#     return 0

# def make_board(board, visited):
#     total_count = 0
#     count = 0
#     for x in range(n):
#         for y in range(n):
#             if count == n:
#                 print(board)
#                 total_count += 1
#             f = check_cross(x, y, visited)
#             if f == 1:
#                 continue
#             elif f == 0:
#                 board[x][y] = 1
#                 count += 1
#                 # print(board)
#                 # print(count)
#     return 0
#     # print(board)
#     # print(count)
#     # if count == n:
#     #     return 1
#     # else:
#     #     return 0

# for i in range(n):
#     for j in range(n):
#         visited = [[0]*n for _ in range(n)]
#         visited[i][j] = 1
#         count = 0
#         answer += make_board(board, visited)
# print(answer)

n = int(input())
answer = 0
row = [0]*n

def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x]-row[i]) == abs(x-i):
            return False
    return True

def n_queen(x):
    global answer
    if x == n:
        answer += 1
        return
    
    for i in range(n):
        row[x] = i
        
        if is_promising(x):
            n_queen(x+1)

n_queen(0)
print(answer)