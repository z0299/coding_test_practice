#완전탐색 알고리즘 공부 - #2606 바이러스
#BFS
#DFS로도 풀 수 있다.
import sys
from collections import deque
input = sys.stdin.readline
cnt = 0 #글로벌 변수 선언 시 가장 앞에 선언

def BFS():
    queue = deque()
    queue.append(network[1])
    while queue:
        network_list = queue.popleft()
        for i in range(1, node_num+1):
            if not virus[i] and network_list[i] == 1:
                queue.append(network[i])
                virus[i] = True
    print(virus.count(True)-1)  #count: virus 리스트에서 True의 개수 구하기

def DFS(start):
    global cnt  #함수 안에서 전역 변수의 값을 변경하려면 global키워드로 선언해주어야 한다.
    virus[start] = True
    for i in range(1, node_num+1):
        if not virus[i] and network[start][i] == 1:
            DFS(i)
            cnt += 1

node_num = int(input())
network_num = int(input())
network = [[0]*(node_num+1) for _ in range(node_num+1)]

for _ in range(network_num):
    n1, n2 = map(int, input().split())
    network[n1][n2] = 1
    network[n2][n1] = 1

virus = [False]*(node_num+1)

BFS()
DFS(1)
print(cnt)