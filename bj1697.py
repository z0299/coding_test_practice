#완전탐색 알고리즘 공부 - #1697 숨바꼭질

import sys
from collections import deque
input = sys.stdin.readline

def BFS(n):
    queue = deque()
    visited_list = [0]*100001   #100000번째 길까지 있기 때문에 100001개 만들어줘야함.
    queue.append(n)
    
    while queue:
        n = queue.popleft()
        if n == k:
            print(visited_list[n])
            exit()
        for i in range(3):
            if i != 2:
                nx = n + move[i]
            elif i == 2:
                nx = n*move[i]
            if 0 <= nx <= 100000 and not visited_list[nx]:  #if문 사용시 앞의 조건부터 검사하기 때문에 순서 바뀌는 경우 index error날 수 있음.
                visited_list[nx] = visited_list[n] + 1
                queue.append(nx)

n, k = map(int,input().split())
move = [-1, 1, 2]
BFS(n)
"""
얘가 성립하지 않는 test case : n == k 로 주어질 때 0 초가 걸려야 하는데 2초가 나온다.

import sys
from collections import deque
input = sys.stdin.readline

def BFS(n):
    queue = deque()
    visited_list = [0]*100001
    queue.append(n)
    
    while queue:
        n = queue.popleft()
        for i in range(3):
            if i != 2:
                nx = n + move[i]
            elif i == 2:
                nx = n*move[i]
            if nx == k:
                print(max(visited_list))
                exit()
            elif 0 <= nx <= 100000 and not visited_list[nx]:
                visited_list[nx] = visited_list[n] + 1
                queue.append(nx)

n, k = map(int,input().split())
move = [-1, 1, 2]
BFS(n)
"""