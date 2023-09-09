def solutions(scores, darts):
    answer = 0
    visited = [[0]*5 for _ in range(5)]
    score = 0
    col = [[] for _ in range(5)]
    
    for i in range(len(darts)):
        x, y = darts[i]//5, (darts[i]%5)-1
        if (x, y) not in col[y]:
            col[y].append((x, y))
        if not visited[x][y]:
            visited[x][y] = 1
            score += scores[x][y]
            
    bingo = 0
    for i in range(5):
        if len(col[i]) == 5:
            bingo += 10
        if 0 not in visited[i]:
            bingo += 10
    
    plus_dart = len(darts) - 5
    start = -10 + (plus_dart*(-5))
    
    answer = start + bingo + score
    return answer