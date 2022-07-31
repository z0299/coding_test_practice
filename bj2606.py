#완전탐색 알고리즘 공부 - #2606 바이러스
#BFS
import sys
from collections import deque
input = sys.stdin.readline

def BFS():
    queue = deque()
    queue.append(network[1])
    while queue:
        network_list = queue.popleft()
        for i in range(1, node_num+1):
            if not virus[i] and network_list[i] == 1:
                queue.append(network[i])
                virus[i] = True
    print(virus.count(True)-1)

node_num = int(input())
network_num = int(input())
network = [[0]*(node_num+1) for _ in range(node_num+1)]

for _ in range(network_num):
    n1, n2 = map(int, input().split())
    network[n1][n2] = 1
    network[n2][n1] = 1

virus = [False]*(node_num+1)

BFS()