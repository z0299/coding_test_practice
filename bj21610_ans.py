# 입력
n, m = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(n)]
move_list = [tuple(map(int, input().split())) for _ in range(m)]

# 8방향
dx8 = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy8 = [0, -1, -1, 0, 1, 1, 1, 0, -1]

# 대각 4방향
dx = [-1, -1, 1, 1]
dy = [-1, 1, -1, 1]

clouds = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]

# move 개수만큼 시행
for d, s in move_list:
    # 모든 구름 이동
    moved_clouds = []
    for x, y in clouds:
        # 구름들을 d 방향으로 s만큼 이동 (구름의 좌표는 연결되어있으므로 %n)
        nx = (x + dx8[d] * s) % n
        ny = (y + dy8[d] * s) % n
        A[nx][ny] += 1 # 물의 양 추가
        moved_clouds.append((nx, ny))
    
    # 이동한 구름들의 대각 4방향을 조사하여 count만큼 물 추가
    for x, y in moved_clouds:
        count = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and A[nx][ny]:
                count += 1
        A[x][y] += count
        
    new_clouds = []
    for x in range(n):
        for y in range(n):
            if (x, y) not in moved_clouds and A[x][y] >= 2:
                A[x][y] -= 2
                new_clouds.append((x, y))
    clouds = new_clouds
    
result = 0
for x in range(n):
    result += sum(A[x])
print(result)

            