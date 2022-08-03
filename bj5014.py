#완전탐색 알고리즘 공부 - #5014 스타트링크
#BFS

import sys
from collections import deque
input = sys.stdin.readline

def BFS(s):
    q = deque()
    q.append(s)
    visited[s] = 1
    
    while q:
        s = q.popleft()
        if s == g:
            return visited[s]-1
        for i in range(2):
            ns = s + change[i]
            if 1 <= ns <= f and not visited[ns]:
                visited[ns] = visited[s] + 1
                q.append(ns)

f, s, g, u, d = map(int, input().split())
change = [u, -d]
visited = [0]*(f+1)

buttons = BFS(s)
if buttons == None:
    print("use the stairs")
else:
    print(buttons)
