#완전탐색 알고리즘 공부 - #1260 DFS와 BFS

#list.pop()은 시간복잡도가 O(N)이다. 따라서 더 빠른 deque를 사용해 시간 절약
import sys
from collections import deque

def DFS(start):
    visited[start] = True   #방문한 노드는 True로 변환하여 재방문하지 않도록 한다
    print(start, end=" ")
    for i in range(1, node+1):
        if not visited[i] and graph[start][i] == 1: #visited의 초기 설정이 False이므로 not False일 때 if문을 만족한다.
            DFS(i)  #재귀로 돌며 dfs 길 찾아감
    
def BFS(start):
    visited[start] = False  #DFS에서 visited을 True로 모두 바꿔놓았기 때문에 BFS를 돌 때는 False로 바꾼다.
    #queue = list()
    queue = deque() #BFS사용 시 deque를 쓴다.
    queue.append(start)
    while queue:
        #start = queue.pop(0)
        start = queue.popleft()
        print(start, end=" ")
        for i in range(1,node+1):
            if visited[i] and graph[start][i] == 1:
                queue.append(i)
                visited[i] = False
    
node, edge, start = map(int, sys.stdin.readline().split())
graph = [[0]*(node+1) for _ in range(node+1)]
#N=4일 때, graph=[[0 0 0 0 0],[0 0 0 0 0],[0 0 0 0 0],[0 0 0 0 0],[0 0 0 0 0]] / 첫원소자리(0)은 사용하지 않음
visited = [False]*(node+1)
#visited=[False, False, False, False, False]

for i in range(edge):
    n1, n2 = map(int, sys.stdin.readline().split())
    #양방향 그래프이기 때문에 n1->n2, n2->n1 둘 다 허용 / 1은 연결되어있다는 의미이다.
    graph[n1][n2] = 1
    graph[n2][n1] = 1

DFS(start)
print()
BFS(start)