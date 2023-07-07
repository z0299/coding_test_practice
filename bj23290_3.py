# 11:40 ~
"""
m, s = map(int, input().split())
fish = [list(map(int, input().split())) for _ in range(m)]
shark = list(map(int, input().split()))

f_dx = [0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [-1, -1, 0, 1, 1, 1, 0, -1]
s_dx = [-1, 0, 1, 0]
s_dy = [0, -1, 0, 1]
smell = []
smell_location = []

for _ in range(s):
    # 1 - 물고기 이동
    old_fish = fish
    new_fish = []
    for f in fish:
        for i in range(8):
            # print(((f[2]-1)+i)%8)
            nx = f[0] + f_dx[((f[2]-1)-i)%8]
            ny = f[1] + f_dy[((f[2]-1)-i)%8]
            if 1 <= nx <= 4 and 1 <= ny <= 4 and [nx, ny] not in smell_location and [nx, ny] != shark:
                # print(nx, ny)
                new_fish.append([nx, ny, ((f[2]-1)-i)%8+1])
                break
            elif i == 7:
                new_fish.append([f[0], f[1], f[2]])
            else:
                continue
        
    # print(new_fish)
    fish = new_fish
    fish_location = [[a[0], a[1]] for a in fish]
    
    # 2 - 상어 이동
    move = 1111
    fish_list = []
    for i in range(4):
        for j in range(4):
            for k in range(4):
                print(i, j, k, shark)
                temp_fish = []
                nx = shark[0] + s_dx[k]
                ny = shark[1] + s_dy[k]
                # print(nx, ny)
                if nx < 1 or nx > 4 or ny < 1 or ny > 4:
                    continue
                elif [nx, ny] in fish_location and [nx, ny] not in temp_fish:
                    temp_fish.append([nx, ny])
                # print(f'1: {nx} {ny}')
                
                nx += s_dx[j]
                ny += s_dy[j]
                if nx < 1 or nx > 4 or ny < 1 or ny > 4:
                    break
                elif [nx, ny] in fish_location and [nx, ny] not in temp_fish:
                    temp_fish.append([nx, ny])
                # print(f'2: {nx} {ny}')

                nx += s_dx[i]
                ny += s_dy[i]
                if nx < 1 or nx > 4 or ny < 1 or ny > 4:
                    break
                elif [nx, ny] in fish_location and [nx, ny] not in temp_fish:
                    temp_fish.append([nx, ny])
                print(f'3: {nx} {ny}')
                
                temp_move = int(str(i+1)+str(j+1)+str(k+1))
                
                # print(move, temp_move, fish_list, temp_fish)
                if len(fish_list) <= len(temp_fish) and move > temp_move:
                    
                    move = temp_move
                    fish_list = temp_fish
                    shark[0] += (s_dx[i]+s_dx[j]+s_dx[k])
                    shark[1] += (s_dy[i]+s_dy[j]+s_dy[k])
    # print(move, shark, fish_list)
    
    # 물고기 삭제 및 냄새 남기기
    for i in range(len(fish_list)):
        for f in fish[:]:
            if f[0] == fish_list[i][0] and f[1] == fish_list[i][1]:
                fish.remove(f)
        fish_location.remove([fish_list[i][0], fish_list[i][1]])
        smell.append([fish_list[i][0], fish_list[i][1], 0])
        smell_location.append([fish_list[i][0], fish_list[i][1]])
    # print(fish, fish_location, smell)
    
    
    # 3
    for s in smell[:]:
        s[2] += 1
        if s[2] == 3:
            x, y = s[0], s[1]
            smell.remove(s)
            smell_location.remove([x, y])
    # print(smell)
    
    # 4
    for i in range(len(old_fish)):
        fish.append(old_fish[i])
    print(fish, smell, shark)
    # print(smell)
"""
n,magic = map(int,input().split())
fish = [list(map(lambda x:int(x)-1,input().split())) for _ in range(n)]
sx,sy = map(lambda x:int(x)-1,input().split())

fish_d = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]
shark_d = [(-1,0),(0,-1),(1,0),(0,1)]
smell = [[-5 for _ in range(4)] for _ in range(4)]

for turn in range(magic):
    # 1 - 물고기 복제 및 이동
    g = [[[] for _ in range(4)] for _ in range(4)]
    saved_fish = fish[:]  # 물고기 복제
    for i in range(len(fish)):
        x,y,d = fish[i]
        for j in range(8):
            nx = x + fish_d[(d-j)%8][0]
            ny = y + fish_d[(d-j)%8][1]
            if 0<=nx<4 and 0<=ny<4 and smell[nx][ny]+2 < turn and (nx,ny) != (sx,sy):
                g[nx][ny] += [(d-j)%8]
                break
        else:
            g[x][y] += [d]

    # 2 - 상어 이동
    ans = -1
    for a in range(4):
        for b in range(4):
            for c in range(4):
                v = [[0 for _ in range(4)] for _ in range(4)]
                tempx, tempy = sx, sy
                temp = 0
                for i in (a,b,c):
                    nx = tempx + shark_d[i][0]
                    ny = tempy + shark_d[i][1]
                    if (0<=nx<4 and 0<=ny<4) == False:
                        break
                    if g[nx][ny] != []:
                        if v[nx][ny] == 0:  # 이미 방문했던 위치의 물고기는 제외
                            temp += len(g[nx][ny])
                    v[nx][ny] = 1
                    tempx, tempy = nx, ny
                else:
                    if ans < temp:
                        ans = temp
                        shark_movement = [a,b,c]
                        
    for i in shark_movement:
        sx += shark_d[i][0]
        sy += shark_d[i][1]
        if g[sx][sy]:   # 물고기가 있으면 흔적 남기기
            smell[sx][sy] = turn
            g[sx][sy] = []
            
    # 5 - 복제
    for x, y, d in saved_fish:
        g[x][y] += [d]
    
    # 저장된 물고기 리스트 새로 만들기
    fish = []
    for i in range(4):
        for j in range(4):
            if g[i][j] != []:
                for k in g[i][j]:
                    fish.append((i,j,k))
                    
print(len(fish))