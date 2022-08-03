#완전탐색 알고리즘 공부 - #2644 촌수계산
#다시풀어보기
import sys
from collections import deque
input = sys.stdin.readline
"""
def BFS(start):
    queue = deque()
    count = -1
    queue.append(start)
    while queue:
        x = queue.popleft()
        count += 1
        for y in range(node+1):
            if end in relations[x]:
                print(count)
                exit()
            if relations[x][y] == 1 and not visited_node[y]:
                visited_node[y] = True
                queue.append(y)
"""

def DFS(x):
    for y in range(node+1):
        if y == end and relations[x][y] == 1:
            visited_node[y] = visited_node[x] + 1
            print(visited_node[y]-1)
            exit()
        elif relations[x][y] == 1 and not visited_node[y]:
            visited_node[y] = visited_node[x] + 1
            DFS(y)
        else:
            continue
    
node = int(input())
start, end = map(int, input().split())
relations_num = int(input())
relations = [[0]*(node+1) for _ in range(node+1)]
for _ in range(relations_num):
    n1, n2 = map(int, input().split())
    relations[n1][n2] = 1
    relations[n2][n1] = 1
visited_node = [0]*(node+1)
visited_node[start] = 1

#BFS(start)
DFS(start)
print(-1)