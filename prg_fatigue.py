answer = -1
def dfs(i, depth, k, dungeons, visited):
    global answer
    if depth > answer:
        answer = depth
    
    visited[i] = 1
    k -= dungeons[i][1]
    # print(visited, k)
    for j in range(len(dungeons)):
        # print(j, visited[j], dungeons[j][0], k, depth)
        if not visited[j] and k >= dungeons[j][0]:
            dfs(j, depth+1, k, dungeons, visited)
            visited[j] = 0
        
    return 

def solution(k, dungeons):
    visited = [0]*len(dungeons)
    for i in range(len(dungeons)):
        dfs(i, 1, k, dungeons, visited)
        visited[i] = 0
    return answer