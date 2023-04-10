# 와 대박 개소름... 15, 16줄 처럼 나눗셈할 때, 숫자로 하드코딩안하고 입력값으로 코딩하는거 주의..!!!!
# 심지어 모든테케가 n이 5였어...
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
move_list = [list(map(int, input().split())) for _ in range(m)]
dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
d_dx = [1, 1, -1, -1]
d_dy = [1, -1, 1, -1]
clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

def cloud_move_and_rain(clouds, move):
    global board
    moved_clouds = []
    for cloud in clouds:
        nx = (cloud[0]+(dx[move[0]]*move[1]))%n
        ny = (cloud[1]+(dy[move[0]]*move[1]))%n
        # nx = (cloud[0]+(dx[move[0]]*move[1]))%5
        # ny = (cloud[1]+(dy[move[0]]*move[1]))%5
        board[nx][ny] += 1
        moved_clouds.append((nx, ny))
    return moved_clouds

def water_copy(new_clouds):
    for cloud in new_clouds:
        count = 0
        for i in range(4):
            nx = cloud[0] + d_dx[i]
            ny = cloud[1] + d_dy[i]
            if 0<=nx<n and 0<=ny<n and board[nx][ny] > 0:
                count += 1
        board[cloud[0]][cloud[1]] += count
        
def new_cloud(moved_clouds):
    new_clouds = []
    for x in range(n):
        for y in range(n):
            if board[x][y] >= 2 and ((x, y) not in moved_clouds):
                new_clouds.append((x, y))
                board[x][y] -= 2
    return new_clouds

for move in move_list:
    #실행
    # 1, 2
    moved_clouds = cloud_move_and_rain(clouds, move)
    # 4
    water_copy(moved_clouds)
    # 5
    clouds = new_cloud(moved_clouds)

total_water = 0    
for i in range(n):
    for j in range(n):
        total_water += board[i][j]
print(total_water)