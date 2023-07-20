n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

chicken = []
house = []

for x in range(n):
    for y in range(n):
        if board[x][y] == 1:
            house.append((x, y))
        elif board[x][y] == 2:
            chicken.append((x, y))

answer = 99999
choosen_chicken_house = []
def dfs(depth, idx):
    global answer
    
    if depth == m:
        total = 0
        for h in house:
            temp1 = 9999
            for c in choosen_chicken_house:
                length = abs(h[0] - c[0]) + abs(h[1] - c[1])
                temp1 = min(temp1, length)
            total += temp1
        answer = min(answer, total)
        return
    
    for i in range(idx, len(chicken)):
        choosen_chicken_house.append(chicken[i])
        dfs(depth+1, i+1)
        choosen_chicken_house.pop()
            
dfs(0, 0)
print(answer)