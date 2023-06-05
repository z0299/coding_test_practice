# 10:00 ~
"""
1. 입력값을 받아 sort한다. (출발지, 도착지 순)
2. 이차원 배열을 생성한다 (n행)
3. 입력값을 돌면서 거리의 차에 해당하는 행에 append한다
4. 1행의 합을 돌면서 최대 공간보다 작으면 최종값에 더한다
5. 2-n의 행을 돌면서 최대 공간과 ~n의 합을 비교해 최종값에 더해준다.

대체 왜 이런생각을 했는지 모르겠지만 완전 틀린 접근방식이다. 답지보고 다시 풀자.

n, c = map(int, input().split())
m = int(input())
input_list = [list(map(int, input().split())) for _ in range(m)]
input_list.sort()
matrix = [[] for _ in range(n)]
answer = 0

for i in range(m):
    idx = input_list[i][1] - input_list[i][0]
    matrix[idx].append(input_list[i])
print(matrix)

for boxes in matrix[1]:
    if boxes[2] <= c:
        answer += boxes[2]
print(answer)

for i in range(2, n):
    for j in range(len(matrix[i])):
        box_count = matrix[i][j][2]
        latest_box = 0
        start = matrix[i][j][0]
        end = matrix[i][j][1]
        for x in range(1, i):
            for y in range(len(matrix[x])):
                if start <= matrix[x][y][0] < end and start < matrix[x][y][1] <= end:
                    print(matrix[x][y])
                    latest_box += matrix[x][y][2]
                if latest_box >= c:
                    latest_box = -1
                    break
            if latest_box >= c:
                latest_box = -1
                break
        print(matrix[i][j], latest_box)
        if latest_box != -1:
            answer += (c-latest_box)
print(answer)
"""
# 정렬할 때, 도착지를 기준으로 정렬해주어야 한다!
n, c = map(int, input().split())
m = int(input())
input_list = [list(map(int, input().split())) for _ in range(m)]
input_list.sort(key=lambda x: x[1])
able_box = [c for _ in range(n+1)]
answer = 0
print(input_list)

for s, e, b in input_list:
    min_num = c
    for i in range(s, e):
        min_num = min(min_num, able_box[i])
    min_num = min(min_num, b)
    for i in range(s, e):
        able_box[i] -= min_num
    answer += min_num
        
print(answer)