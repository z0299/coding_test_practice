# dfs, bfs 알고리즘 공부 - 25분

import sys
input = sys.stdin.readline
from collections import deque
queue = deque()

def dfs(nmap, v, dfs_list):
    dfs_list.append(v)
    for i in range(1, len(nmap[v])):
        if nmap[v][i] == 1 and i not in dfs_list:
            dfs(nmap, i, dfs_list)
    return dfs_list

def bfs(v, bfs_list):
    queue.append(v)
    bfs_list.append(v)
    
    while queue:
        node = queue.popleft()
        for i in range(1, len(nmap[node])):
            if nmap[node][i] == 1 and i not in bfs_list:
                bfs_list.append(i)
                queue.append(i)
    return bfs_list
        

if __name__ == "__main__":
    n, m, v = map(int, input().split())
    nmap = [[0]*(n+1) for _ in range((n+1))]
    for _ in range(m):
        a, b = map(int, input().split())
        nmap[a][b] = 1
        nmap[b][a] = 1
    dfs_list = []
    bfs_list = []
    
    dfs_list = dfs(nmap, v, dfs_list)
    bfs_list = bfs(v, bfs_list)
    
    print(' '.join(map(str, dfs_list)))
    print(' '.join(map(str, bfs_list)))