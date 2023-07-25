# 입력값 받기, 토네이도 초기위치 설정
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
tx = ty = n//2

# 토네이도 방향에 맞춰 비율 배열 변경 (반시계 90도)
def rotate_c90(proportion):
    new_proportion = list(map(list, zip(*proportion)))[::-1]
    return new_proportion

p_left = [[0, 0, 0.02, 0, 0], [0, 0.1, 0.07, 0.01, 0], 
        [0.05, 0, 0, 0, 0], [0, 0.1, 0.07, 0.01, 0], 
        [0, 0, 0.02, 0, 0]]
p_down = rotate_c90(p_left)
p_right = rotate_c90(p_down)
p_up = rotate_c90(p_right)
proportions = [p_left, p_down, p_right, p_up]
alphas = [(2, 1), (3, 2), (2, 3), (1, 2)]   # 토네이도 이동방향에 따른 알파 위치

# 토네이도 이동방향
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]

# 초기 세팅
outer_sand = 0
direction = 0
turn = 2        # 토네이도 방향 바꾸는 지표 -> 좌-하 : turn = 2 / 우-상: turn = 4, 2씩 늘어난다.
tornado_length = 0      # 토네이도 직선 길이
proportion = proportions[0]

# 토네이도가 종료될 때 까지 토네이도 이동 -> 모래 이동 -> 토네이도 방향바꾸기 반복
# while tx != 0 and ty != 0:
while not (tx == 0 and ty == 0):
    # print(board, tx, ty, outer_sand)
    # 토네이도 이동
    tx += delta[direction][0]
    ty += delta[direction][1]
    tornado_length += 1     # 토네이도 길이 갱신
    sand = board[tx][ty]
    board[tx][ty] = 0   # 토네이도 위치에 있는 모래는 모두 사라지게 된다
    left = sand     # proportion으로 이동하고 남은 모래
    
    # 모래 이동 (proportion의 y 위치와 data의 토네이도 위치 일치시켜 모래정보 갱신)
    for x in range(5):
        for y in range(5):
            now_sand = int(sand * proportion[x][y])
            left -= now_sand
            if 0 <= tx+x-2 < n and 0 <= ty+y-2 < n:
                board[tx+x-2][ty+y-2] += now_sand
            else:
                outer_sand += now_sand
    
    # alpha 위치에 남은 모래 두기
    if 0 <= tx+alphas[direction][0]-2 < n and 0 <= ty+alphas[direction][1]-2 < n:
        board[tx+alphas[direction][0]-2][ty+alphas[direction][1]-2] += left
    else:
        outer_sand += left
    
    # 토네이도 방향 바꾸기
    if tornado_length == turn // 2 or tornado_length == turn:
        direction = (direction + 1) % 4
        proportion = proportions[direction]
        if tornado_length == turn:
            tornado_length = 0
            turn += 2
    
# 토네이도 종료 후
print(outer_sand)