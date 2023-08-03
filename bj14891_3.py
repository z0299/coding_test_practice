# 4:00 ~ 4:25
from collections import deque

def rotate_right(gear, dir):
    if gear > 4 or gears[gear-1][2] == gears[gear][6]:
        return
    
    if gears[gear-1][2] != gears[gear][6]:
        rotate_right(gear+1, -dir)
        gears[gear].rotate(dir)

def rotate_left(gear, dir):
    if gear < 1 or gears[gear][2] == gears[gear+1][6]:
        return
    
    if gears[gear][2] != gears[gear+1][6]:
        rotate_left(gear-1, -dir)
        gears[gear].rotate(dir)

gears = {}
for i in range(4):
    gears[i+1] = deque(list(map(int, input())))

k = int(input())
rotate = []
for _ in range(k):
    rotate.append(tuple(map(int, input().split())))

for r in rotate:
    gear = r[0]
    dir = r[1]
    
    rotate_right(gear+1, -dir)
    rotate_left(gear-1, -dir)
    gears[gear].rotate(dir)

answer = 0    
for i in range(4):
    if gears[i+1][0] == 0:
        continue
    else:
        answer += 2**i
print(answer)