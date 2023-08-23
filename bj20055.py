# 11:00 ~
def check_durability():
    cnt = 0
    for i in range(2):
        for j in range(n):
            if q[i][j][0] == 0:
                cnt += 1
    return cnt

def rotate():
    temp = q[1][0]
    # 밑 줄 왼쪽으로 한칸씩 이동
    for i in range(1, n):
        q[1][i-1] = q[1][i]
    # 밑줄 오른쪽칸 윗줄 오른쪽 칸에서 받아오기
    q[1][n-1] = q[0][n-1]
    # 윗 줄 오른쪽으로 한칸씩 이동
    for i in range(n-1, 0, -1):
        q[0][i] = q[0][i-1]
    # 윗 줄 첫번째 칸 채우기
    q[0][0] = temp

n, k = map(int, input().split())
q = []
q.append([])
q.append([])

cnt = 0
for i in map(int, input().split()):
    if cnt >= n:
        # q[1].append([i, 0])
        q[1].insert(0, [i, 0])
    else:
        q[0].append([i, 0])
    cnt += 1

turn = 0
while True:    
    turn += 1
    
    # step 1
    rotate()        # 한바퀴 돌리기
    if q[0][n-1][1] == 1:   # 로봇이 있으면 내리기
        q[0][n-1][1] = 0
    
    # step 2
    for i in range(n-2, 0, -1):
        if q[0][i][1] == 1 and q[0][i+1][1] == 0 and q[0][i+1][0] > 0:  # 로봇이 있을 때 이동하려는 칸에 로봇이 없고 내구도가 1 이상이면
            # 로봇 옮기기
            if i+1 != n-1:
                q[0][i+1][1] = 1
            q[0][i][1] = 0
            
            # 내구도 감소
            q[0][i+1][0] -= 1
    
    # step 3
    if q[0][0][0] > 0:  # 내구도가 1 이상이라면
        q[0][0][1] = 1      # 로봇 두기
        q[0][0][0] -= 1     # 내구성 감소
    
    # step 4
    if check_durability() >= k:
        print(turn)
        break