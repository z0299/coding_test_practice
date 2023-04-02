# 구현 알고리즘 공부 - 17분

import sys
input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
x = 1
y = 1
route = list(input().split())

for i in range(len(route)):
    if route[i] == 'U':
        if x+dx[0] >= 1 and y+dy[0] >= 1:
            x += dx[0]
            y += dy[0]
        else:
            continue
    elif route[i] == 'D':
        if x+dx[1] >= 1 and y+dy[1] >= 1:
            x += dx[1]
            y += dy[1]
        else:
            continue
    elif route[i] == 'L':
        if x+dx[2] >= 1 and y+dy[2] >= 1:
            x += dx[2]
            y += dy[2]
        else:
            continue
    else:
        if x+dx[3] >= 1 and y+dy[3] >= 1:
            x += dx[3]
            y += dy[3]
        else:
            continue
print(x, y)

"""이렇게 푸는게 맞는 것 같다.
n = int(input())
x, y = 1, 1
routes = input().split()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
move_types = ['U', 'D', 'L', 'R']

for route in routes:
    for i in range(len(move_types)):
        if route == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    # 이동 수행
    x, y = nx, ny
    
print(x, y)
"""