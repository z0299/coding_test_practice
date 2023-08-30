def dfs(x, temp, n, computers):
    temp.add(x)
    
    for i in range(n):
        if computers[x][i] == 1 and x != i and i not in temp:
            dfs(i, temp, n, computers)
    return

def solution(n, computers):
    answer = 0
    
    networks = []
    visited = [0]*n
    
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1 and not visited[i] and not visited[j]:
                temp = set()
                temp.add(i)
                dfs(j, temp, n, computers)
                networks.append(temp)
                for k in temp:
                    visited[k] = 1
    
    for i in range(n):
        if visited[i] == 0:
            answer += 1
    answer += len(networks)
    return answer