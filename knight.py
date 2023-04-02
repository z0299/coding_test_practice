# 구현 알고리즘 공부 - 12분
axis = list(input())

if axis[0] == 'a':
    x = 1
elif axis[0] == 'b':
    x = 2
elif axis[0] == 'c':
    x = 3
elif axis[0] == 'd':
    x = 4
elif axis[0] == 'e':
    x = 5
elif axis[0] == 'f':
    x = 6
elif axis[0] == 'g':
    x = 7
elif axis[0] == 'h':
    x = 8
else:
    exit()
y = int(axis[1])
count = 0

dx = [-1, 1, 2, 2, 1, -1, -2, -2]
dy = [-2, -2, -1, 1, 2, 2, 1, -2]

for i in range(len(dx)):
    if x+dx[i] >= 1 and x+dx[i] <=8 and y+dy[i] >= 1 and y+dy[i] <= 8:
        count += 1
    else:
        continue
print(count)

"""
input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1

steps = [(-2,-1), (-1, -2), (1,-2), (2,-1), (2,1), (1,2), (-1,2), (-2,1)]

result = 0
for step in steps:
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
        result += 1
print(result)
"""