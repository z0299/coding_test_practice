n, m = map(int, input().split())
x, y, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

print(x, y, d)
print(map)
# count = 0
# while True:
#     # 1
#     if map[x][y] == 0:
#         count += 1
#         map[x][y] = 3
        
#     # 3
#     while count < 2:
#         dirty_room = 0
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
#                 print(count)
#                 print(nx, ny)
#                 dirty_room += 1
#                 d = (d+3)%4
#                 nnx = nx + dx[d]
#                 nny = ny + dy[d]
#                 if 0 <= nnx < n and 0 <= nny < m and map[nnx][nny] == 0:
#                     x = nnx
#                     y = nny
#                 break
        
#     # 2
#     if dirty_room == 0:
#         nd = (d+2)%4
#         nx = x + dx[nd]
#         ny = y + dy[nd]
#         if 0 <= nx < n and 0 <= ny < m and map[nx][ny] == 0:
#             x = nx
#             y = ny
#         else:
#             break

print(count)