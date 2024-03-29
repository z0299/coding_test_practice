n = int(input())
students = [list(map(int, input().split())) for _ in range(n**2)]
dict = {}
for i in range(n**2):
    dict.update({students[i][0]-1:list(map(lambda a: a-1, students[i][1:]))})

board = [[-1]*n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for stu in dict:
    seat = [(100, 100), 0, 0]     # 좌표, 친구, 빈칸
    for x in range(n):
        for y in range(n):
            # 빈칸에 대해 주변의 친구 수, 빈자리 수를 계산
            if board[x][y] == -1:
                friends = 0
                empty = 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in dict[stu]:
                            friends += 1
                        elif board[nx][ny] == -1:
                            empty += 1
                
                # 1, 2, 3 조건에 의한 자리 배정
                if friends > seat[1]:
                    seat = [(x, y), friends, empty]
                elif friends == seat[1]:
                    if empty > seat[2]:
                        seat = [(x, y), friends, empty]
                    elif empty == seat[2]:
                        if nx < seat[0][0]:
                            seat = [(x, y), friends, empty]
                        elif nx == seat[0][0]:
                            if ny < seat[0][1]:
                                seat = [(x, y), friends, empty]

    board[seat[0][0]][seat[0][1]] = stu
    
# 주변의 친한 친구 수 계산
answer = 0
for x in range(n):
    for y in range(n):
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] in dict[board[x][y]]:
                count += 1
        
        # 점수 계산      
        if count == 0:
            answer += 0
        elif count == 1:
            answer += 1
        elif count == 2:
            answer += 10
        elif count == 3:
            answer += 100
        elif count == 4:
            answer += 1000
            
print(answer)