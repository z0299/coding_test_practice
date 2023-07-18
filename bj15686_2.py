n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
answer = 99999

chicken = []
house = []
choosen_chicken_list = []

for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            house.append((x, y))
        elif board[x][y] == 2:
            chicken.append((x, y))
        
def dfs(depth, idx):
    global answer
    
    if depth == m:
        sum = 0
        # 하우스 당 체크 시작
        for h in house:
            val = 99999
            # 치킨집 순차 탐색
            for choosen_chicken in choosen_chicken_list:
                tmp = abs(h[0]-choosen_chicken[0]) + abs(h[1]-choosen_chicken[1])   # 치킨 거리
                val = min(tmp, val)
            sum += val
        answer = min(answer, sum)
        return
    
    # combination 구현
    for i in range(idx, len(chicken)):
        if chicken[i] in choosen_chicken_list:
            continue
        
        choosen_chicken_list.append(chicken[i])
        dfs(depth+1, i+1)
        choosen_chicken_list.pop()
        
dfs(0, 0)
print(answer)