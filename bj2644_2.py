# bfs 알고리즘 공부 - 1시간.. 못풀었다.... 다시해보기
""" 왜 bfs로 풀려고 했을까? 최단거리라고 생각해서 그랬던 것 같다...
import sys
from collections import deque
queue = deque()
input = sys.stdin.readline

def bfs(pmap, s, e, visited, plist):
    queue.append(s)
    visited[s] = 1
    while queue:
        c = queue.popleft()
        if c == e:
            return visited.count(True)
        for i in range(1, len(pmap[c])):
            if pmap[c][i] == 1 and not visited[i]:
                visited[i] = 1
                queue.append(i)
                #print(i)
                
    return -1
    
if __name__ == "__main__":
    n = int(input())
    pmap = [[0]*(n+1) for _ in range(n+1)]
    start, end = map(int, input().split())
    m = int(input())
    plist = []
    for _ in range(m):
        a, b = map(int, input().split())
        plist.append([a, b])
        pmap[a][b] = 1
        pmap[b][a] = 1
    print(pmap)
    visited = [0]*(n+1)
    count = bfs(pmap, start, end, visited, plist)
    print(count)
"""
import sys
input = sys.stdin.readline

def dfs(pmap, start, end, visited):
    for i in range(1, len(pmap[start])):
        if i == end and pmap[start][i] == 1:
            visited[i] = visited[start] + 1
            print(visited[i])
            exit()
        elif pmap[start][i] == 1 and not visited[i]:
            visited[i] = visited[start]+1
            dfs(pmap, i, end, visited)
        else:
            continue
    return -1

if __name__ == "__main__":
    n = int(input())
    pmap = [[0]*(n+1) for _ in range(n+1)]
    start, end = map(int, input().split())
    m = int(input())
    
    for _ in range(m):
        a, b = map(int, input().split())
        pmap[a][b] = 1
        pmap[b][a] = 1
    visited = [0]*(n+1)
    count = dfs(pmap, start, end, visited)
    print(count)