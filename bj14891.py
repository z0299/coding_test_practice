# 5:00 ~
gear = []
for _ in range(4):
    gear.append(list(map(int, input())))
k = int(input())
rotation = [tuple(map(int, input().split())) for _ in range(k)]

def rotate_clockwise(gear):
    new_gear = []
    new_gear.append(gear[-1])
    for i in range(0, 7):
        new_gear.append(gear[i])
    return new_gear

def rotate_counterclock(gear):
    temp = gear[0]
    gear.append(temp)
    return gear[1:]

for i in range(k):
    rotate_gear = rotation[i][0]-1
    rotate_dir = rotation[i][1]

    if rotate_gear == 0:    # 첫째 기어
        if gear[0][2] == gear[1][6]:    # 첫번째가 같으면 1번 기어만 돌리기
            if rotate_dir == 1:
                gear[0] = rotate_clockwise(gear[0])
            else:
                gear[0] = rotate_counterclock(gear[0])
        else:
            if gear[1][2] == gear[2][6]:    # 두번째가 같으면 1, 2번 기어 돌리기
                if rotate_dir == 1:
                    gear[0] = rotate_clockwise(gear[0])
                    gear[1] = rotate_counterclock(gear[1])
                else:
                    gear[0] = rotate_counterclock(gear[0])
                    gear[1] = rotate_clockwise(gear[1])
            else:       
                if gear[2][2] == gear[3][6]:    # 세번째가 같으면 1, 2, 3번 기어 돌리기
                    if rotate_dir == 1:
                        gear[0] = rotate_clockwise(gear[0])
                        gear[1] = rotate_counterclock(gear[1])
                        gear[2] = rotate_clockwise(gear[2])
                    else:
                        gear[0] = rotate_counterclock(gear[0])
                        gear[1] = rotate_clockwise(gear[1])
                        gear[2] = rotate_counterclock(gear[2])
                else:           # 세번째까지 다르면 1, 2, 3, 4번 기어 돌리기
                    if rotate_dir == 1:
                        gear[0] = rotate_clockwise(gear[0])
                        gear[1] = rotate_counterclock(gear[1])
                        gear[2] = rotate_clockwise(gear[2])
                        gear[3] = rotate_counterclock(gear[3])
                    else:
                        gear[0] = rotate_counterclock(gear[0])
                        gear[1] = rotate_clockwise(gear[1])
                        gear[2] = rotate_counterclock(gear[2])
                        gear[3] = rotate_clockwise(gear[3])
    elif rotate_gear == 1:      # 두번째 기어
        if gear[1][6] == gear[0][2] and gear[1][2] == gear[2][6]:
            if rotate_dir == 1:
                gear[1] = rotate_clockwise(gear[1])
            else:
                gear[1] = rotate_counterclock(gear[1])
        elif gear[1][6] != gear[0][2] and gear[1][2] == gear[2][6]:
            if rotate_dir == 1:
                gear[1] = rotate_clockwise(gear[1])
                gear[0] = rotate_counterclock(gear[0])
            else:
                gear[1] = rotate_counterclock(gear[1])
                gear[0] = rotate_clockwise(gear[0])
        elif gear[1][6] == gear[0][2] and gear[1][2] != gear[2][6]:
            if gear[2][2] == gear[3][6]:
                if rotate_dir == 1:
                    gear[1] = rotate_clockwise(gear[1])
                    gear[2] = rotate_counterclock(gear[2])
                else:
                    gear[1] = rotate_counterclock(gear[1])
                    gear[2] = rotate_clockwise(gear[2])
            else:
                if rotate_dir == 1:
                    gear[1] = rotate_clockwise(gear[1])
                    gear[2] = rotate_counterclock(gear[2])
                    gear[3] = rotate_clockwise(gear[3])
                else:
                    gear[1] = rotate_counterclock(gear[1])
                    gear[2] = rotate_clockwise(gear[2])
                    gear[3] = rotate_counterclock(gear[3])
        else:
            if gear[2][2] == gear[3][6]:
                if rotate_dir == 1:
                    gear[0] = rotate_counterclock(gear[0])
                    gear[1] = rotate_clockwise(gear[1])
                    gear[2] = rotate_counterclock(gear[2])
                else:
                    gear[0] = rotate_clockwise(gear[0])
                    gear[1] = rotate_counterclock(gear[1])
                    gear[2] = rotate_clockwise(gear[2])
            else:
                if rotate_dir == 1:
                    gear[0] = rotate_counterclock(gear[0])
                    gear[1] = rotate_clockwise(gear[1])
                    gear[2] = rotate_counterclock(gear[2])
                    gear[3] = rotate_clockwise(gear[3])
                else:
                    gear[0] = rotate_clockwise(gear[0])
                    gear[1] = rotate_counterclock(gear[1])
                    gear[2] = rotate_clockwise(gear[2])
                    gear[3] = rotate_counterclock(gear[3])
    elif rotate_gear == 2:      # 세번째 기어
        if gear[2][6] == gear[1][2] and gear[2][2] == gear[3][6]:
            if rotate_dir == 1:
                gear[2] = rotate_clockwise(gear[2])
            else:
                gear[2] = rotate_counterclock(gear[2])
        elif gear[2][6] == gear[1][2] and gear[2][2] != gear[3][6]:
            if rotate_dir == 1:
                gear[2] = rotate_clockwise(gear[2])
                gear[3] = rotate_counterclock(gear[3])
            else:
                gear[2] = rotate_counterclock(gear[2])
                gear[3] = rotate_clockwise(gear[3])
        elif gear[2][6] != gear[1][2] and gear[2][2] == gear[3][6]:
            if gear[0][2] == gear[1][6]:
                if rotate_dir == 1:
                    gear[2] = rotate_clockwise(gear[2])
                    gear[1] = rotate_counterclock(gear[1])
                else:
                    gear[2] = rotate_counterclock(gear[2])
                    gear[1] = rotate_clockwise(gear[1])
            else:
                if rotate_dir == 1:
                    gear[2] = rotate_clockwise(gear[2])
                    gear[1] = rotate_counterclock(gear[1])
                    gear[0] = rotate_clockwise(gear[0])
                else:
                    gear[2] = rotate_counterclock(gear[2])
                    gear[1] = rotate_clockwise(gear[1])
                    gear[0] = rotate_counterclock(gear[0])
        else:
            if gear[0][2] == gear[1][6]:
                if rotate_dir == 1:
                    gear[1] = rotate_counterclock(gear[1])
                    gear[2] = rotate_clockwise(gear[2])
                    gear[3] = rotate_counterclock(gear[3])
                else:
                    gear[1] = rotate_clockwise(gear[1])
                    gear[2] = rotate_counterclock(gear[2])
                    gear[3] = rotate_clockwise(gear[3])
            else:
                if rotate_dir == 1:
                    gear[0] = rotate_clockwise(gear[0])
                    gear[1] = rotate_counterclock(gear[1])
                    gear[2] = rotate_clockwise(gear[2])
                    gear[3] = rotate_counterclock(gear[3])
                else:
                    gear[0] = rotate_counterclock(gear[0])
                    gear[1] = rotate_clockwise(gear[1])
                    gear[2] = rotate_counterclock(gear[2])
                    gear[3] = rotate_clockwise(gear[3])
    elif rotate_gear == 3:      # 네번째 기어
        if gear[2][2] == gear[3][6]:
            if rotate_dir == 1:
                gear[3] = rotate_clockwise(gear[3])
            else:
                gear[3] = rotate_counterclock(gear[3])
        else:
            if gear[1][2] == gear[2][6]:
                if rotate_dir == 1:
                    gear[2] = rotate_counterclock(gear[2])
                    gear[3] = rotate_clockwise(gear[3])
                else:
                    gear[2] = rotate_clockwise(gear[2])
                    gear[3] = rotate_counterclock(gear[3])
            else:
                if gear[0][2] == gear[1][6]:
                    if rotate_dir == 1:
                        gear[1] = rotate_clockwise(gear[1])
                        gear[2] = rotate_counterclock(gear[2])
                        gear[3] = rotate_clockwise(gear[3])
                    else:
                        gear[1] = rotate_counterclock(gear[1])
                        gear[2] = rotate_clockwise(gear[2])
                        gear[3] = rotate_counterclock(gear[3])
                else:
                    if rotate_dir == 1:
                        gear[0] = rotate_counterclock(gear[0])
                        gear[1] = rotate_clockwise(gear[1])
                        gear[2] = rotate_counterclock(gear[2])
                        gear[3] = rotate_clockwise(gear[3])
                    else:
                        gear[0] = rotate_clockwise(gear[0])
                        gear[1] = rotate_counterclock(gear[1])
                        gear[2] = rotate_clockwise(gear[2])
                        gear[3] = rotate_counterclock(gear[3])

answer = 0
if gear[0][0] == 1:
    answer += 1
if gear[1][0] == 1:
    answer += 2
if gear[2][0] == 1:
    answer += 4
if gear[3][0] == 1:
    answer += 8
print(answer)