# brute-force 문제였다..

n = int(input())
board = [list(input()) for _ in range(n)]
max_count = 0

# 열이 다를 때
for i in range(n):
    for j in range(n-1):
        if board[i][j] != board[i][j+1]:
            board[i]