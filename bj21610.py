# 이동 구현할 때, n 다음 1붙이는 거를 모르겠었다.
n, m = map(int, input().split())
A = []
for i in range(n):
    A.append(list(map(int, input().split())))
    A[i].insert(0, 0)
A.insert(0, [0]*(n+1))
move_list = []
for i in range(m):
    move_list.append(list(map(int, input().split())))

dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
d_dx = [-1, -1, 1, 1]
d_dy = [-1, 1, 1, -1]
cloud_list = [[n,1], [n,2], [n-1,1], [n-1,2]]

def cloud_move(move, visited):
    global cloud_list
    for cloud in cloud_list:
        nx = cloud[0] + (dx[move[0]]*move[1])
        ny = cloud[1] + (dy[move[0]]*move[1])
        if nx % 5 == 0:
            nx = (nx % 5) + 5
        else:
            nx = nx % 5
        if ny % 5 == 0:
            ny = (ny % 5) + 5
        else:
            ny = ny % 5
        cloud[0] = nx
        cloud[1] = ny
        A[nx][ny] += 1
        visited[nx][ny] = 1
    return cloud_list, visited
            
# def plus_one(cloud_list):
#     global A
#     for i in range(len(cloud_list)):
#         A[cloud_list[i][0]][cloud_list[i][1]] += 1
            
def water_copy_bug():
    for cloud in cloud_list:
        water_copy = 0
        for i in range(4):
            nx = cloud[0] + d_dx[i]
            ny = cloud[1] + d_dy[i]
            if 0<nx<=n and 0<ny<=n and (A[nx][ny] > 0):
                water_copy += 1
        A[cloud[0]][cloud[1]] += water_copy
        
def cloud_make(visited):
    temp_cloud_list = []
    for i in range(1, n+1):
        for j in range(1, n+1):
            #if A[i][j] >= 2 and ([i, j] not in cloud_list):
            if A[i][j] >= 2 and not visited[i][j]:
                temp_cloud_list.append([i, j])
                A[i][j] -= 2
    return temp_cloud_list
    
for i in range(len(move_list)):
    # 1
    visited = [[0]*(n+1) for _ in range(n+1)]
    cloud_list, visited = cloud_move(move_list[i], visited)

    # 2
    #plus_one(cloud_list)

    # 3
    # 5번이 끝나고 수행
    
    # 4
    water_copy_bug()

    # 5
    cloud_list = cloud_make(visited)


total_water = 0
#for i in range(n+1):
#    for j in range(n+1):
#        total_water += A[i][j]
for i in range(1, n+1):
    total_water += sum(A[i])
print(total_water)