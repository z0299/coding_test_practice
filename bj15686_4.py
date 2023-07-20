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
            
choosen_chicken = []
answer = 9999
def dfs(idx):
    global answer
    
    if len(choosen_chicken) == m:
        temp = 0
        for h in house:
            length = 9999
            for c in choosen_chicken:
                length = min(length, abs(h[0]-c[0]) + abs(h[1]-c[1]))
            temp += length
        answer = min(answer, temp)
        return
    
    for i in range(idx, len(chicken)):
        choosen_chicken.append(chicken[i])
        dfs(i+1)
        choosen_chicken.pop()

dfs(0)
print(answer)
