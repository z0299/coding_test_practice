import copy

f_dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
f_dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
c_dx = [0, 0, 1, 1, 1, 0, -1, -1, -1]
c_dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]
s_dx = [0, -1, 0, 1, 0]
s_dy = [0, 0, -1, 0, 1]

def fish_move(fish_map, my_map, shark_x, shark_y):
    """
    for i in range(len(fish_map)):
        x = fish_map[i][0] + f_dx[fish_map[i][2]]
        y = fish_map[i][1] + f_dy[fish_map[i][2]]
        count = 1
        while (x<=0 or x>4 or y<=0 or y>4) or (type(my_map[x][y]) is list) or (x==shark_x and y==shark_y):
            x = fish_map[i][0] + c_dx[(fish_map[i][2]+count)%8]
            y = fish_map[i][1] + c_dy[(fish_map[i][2]+count)%8]
            count += 1
        my_map[x][y] += 1
    """
    for i in range(len(fish_map)):
        x = fish_map[i][0] + f_dx[fish_map[i][2]]
        y = fish_map[i][1] + f_dy[fish_map[i][2]]
        count = 1
        while (x<=0 or x>4 or y<=0 or y>4) or (type(my_map[x][y]) is list) or (x==shark_x and y==shark_y):
            x = fish_map[i][0] + c_dx[(fish_map[i][2]+count)%8]
            y = fish_map[i][1] + c_dy[(fish_map[i][2]+count)%8]
            fish_map[i][2] = f_dx.(fish_map[i][2]+count)%8
            count += 1
        fish_map[i][0] = x
        fish_map[i][1] = y
        
        my_map[fish_map[i][0]][fish_map[i][1]] += 1
    print(fish_map)
    return fish_map, my_map

def shark_move(my_map, shark_x, shark_y):
    shark_move = []
    for a in range(1, 5):
        for b in range(1, 5):
            for c in range(1, 5):
                shark_move.append([a, b, c])
    eating_fish_list = []
    for i in range(len(shark_move)):
        fish_count = 0
        for j in range(3):
            sx = shark_x + s_dx[shark_move[i][j]]
            sy = shark_y + s_dy[shark_move[i][j]]
            if sx <= 0 or sx > 4 or sy <= 0 or sy > 4:
                eating_fish_list.append(0)
                break
            fish_count += my_map[sx][sy]
        eating_fish_list.append(fish_count)
    
    move = eating_fish_list.index(max(eating_fish_list))
    print(eating_fish_list)
    print(move)
    for i in range(3):
        shark_x += s_dx[shark_move[move][i]]
        shark_y += s_dy[shark_move[move][i]]
        if my_map[shark_x][shark_y]:
            my_map[shark_x][shark_y] = [0]
    #print(eating_fish_list)
    return my_map, shark_x, shark_y

# 값 입력
m, s = map(int, input().split())
my_map = [[0]*5 for _ in range(5)]
fish_map = []
# 물고기 값 받기
for i in range(m):
    fish_map.append(list(map(int, input().split())))
    
shark_x, shark_y = map(int, input().split())

for _ in range(s):
    #1
    copy_map = copy.deepcopy(fish_map)
    print("fish_map")
    print(fish_map)
    
    #2
    fish_map, my_map = fish_move(fish_map, my_map, shark_x, shark_y)
    
    #3
    my_map, shark_x, shark_y = shark_move(my_map, shark_x, shark_y)
    
    #4
    for i in range(5):
        for j in range(5):
            if type(my_map[i][j]) is list:
                if my_map[i][j][0] == 2:
                    my_map[i][j][0] = 0
                else:
                    my_map[i][j][0] += 1
    #5
    for i in range(len(fish_map)):
        my_map[fish_map[i][0]][fish_map[i][1]] += 1
    
#print(fish_map)
print(my_map)
fish_num = 0
for i in range(5):
    for j in range(5):
        if type(my_map[i][j]) is not list:
            fish_num += my_map[i][j]
print(fish_num)
