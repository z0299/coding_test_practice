# python의 rotate 함수를 사용하면 deque를 쉽게 회전시킬 수 있다
# 양수는 오른쪽 회전, 음수는 왼쪽 회전
from collections import deque

gears = {}
for i in range(1, 5):
    gears[i] = deque(map(int, input()))

k = int(input())
rotation = [tuple(map(int, input().split())) for _ in range(k)]

def rotate_right(gear, dir):
    # 회전하지 않는 경우
    if gear > 4 or gears[gear-1][2] == gears[gear][6]:
        return
    
    # 회전하는 경우
    if gears[gear-1][2] != gears[gear][6]:
        rotate_right(gear+1, -dir)      # 재귀
        gears[gear].rotate(dir)
        
def rotate_left(gear, dir):
    if gear < 1 or gears[gear][2] == gears[gear+1][6]:
        return
    
    if gears[gear][2] != gears[gear+1][6]:
        rotate_left(gear-1, -dir)
        gears[gear].rotate(dir)

for i in range(k):
    gear = rotation[i][0]
    dir = rotation[i][1]
    
    rotate_right(gear+1, -dir)
    rotate_left(gear-1, -dir)
    gears[gear].rotate(dir)

answer = 0
if gears[1][0] == 1:
    answer += 1
if gears[2][0] == 1:
    answer += 2
if gears[3][0] == 1:
    answer += 4
if gears[4][0] == 1:
    answer += 8
print(answer)