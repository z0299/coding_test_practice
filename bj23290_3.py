# 11:40 ~
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
                temp_fish = []
                nx = shark[0] + s_dx[i]
                ny = shark[1] + s_dy[i]
                if nx < 1 or nx > 4 or ny < 1 or ny > 4:
                    continue
                elif [nx, ny] in fish_location:
                    temp_fish.append([nx, ny])
                
                nx += s_dx[j]
                ny += s_dy[j]
                if nx < 1 or nx > 4 or ny < 1 or ny > 4:
                    continue
                elif [nx, ny] in fish_location:
                    temp_fish.append([nx, ny])

                nx += s_dx[k]
                ny += s_dy[k]
                if nx < 1 or nx > 4 or ny < 1 or ny > 4:
                    continue
                elif [nx, ny] in fish_location:
                    temp_fish.append([nx, ny])
                
                temp_move = int(str(i+1)+str(j+1)+str(k+1))
                print(move, temp_move, fish_list, temp_fish)
                if len(fish_list) <= len(temp_fish) and move > temp_move:
                    
                    move = temp_move
                    fish_list = temp_fish
                    shark[0] += (s_dx[i]+s_dx[j]+s_dx[k])
                    shark[1] += (s_dy[i]+s_dy[j]+s_dy[k])
    print(move, shark, fish_list)
    
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