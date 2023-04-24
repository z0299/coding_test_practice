"""
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
ans = 2001

start = [i for i in range(n)]
link = []

def get_score(team):
    n = len(team)
    score = 0
    for i in range(n):
        for j in range(n):
            score += board[team[i]][team[j]]
    return score

def dfs():
    global ans
    if len(start) == n//2:
        start_score = get_score(start)
        link_score = get_score(link)
        score = abs(start_score-link_score)
        if ans > score:
            ans = score
        return
    
    for i in range(n):
        if i not in link:
            link.append(start.pop(start.index(i)))
            dfs()
            start.append(link.pop())

dfs()
print(ans)
"""

def dfs(depth, idx):
    global ans
    if depth == n//2:
        start_score, link_score = 0, 0
        
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    start_score += board[i][j]
                elif not visited[i] and not visited[j]:
                    link_score += board[i][j]
                    
        ans = min(ans, abs(start_score-link_score)) 
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
ans = int(1e9)

dfs(0, 0)
print(ans)