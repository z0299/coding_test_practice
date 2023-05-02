# bfs로 풀어야하는 이유?
# 한 노드에 도착했을 때, 거기서 갈 수 있는 모든 방향의 conv를 다 돌아보는게 맞다.
# 한 노드에서 갈 수 있는 모든 노드에 대해서 마지막 도착점에 도달할 수 있다면 끝나기 때문이다.
# 만약 bfs를 안쓰고 순서대로 돈다면, 목적지에 도달 할 수 있었음에도 도달하지 못할 수 있다.
"""
Try #1
t = int(input())
for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    conv = []
    for _ in range(n):
        conv.append(list(map(int, input().split())))
    conv.sort()
    end = list(map(int, input().split()))
    beer = 20
    
    # 편의점 들리기
    for i in range(n):
        length_x = abs(conv[i][0] - start[0])
        length_y = abs(conv[i][1] - start[1])
        #print(length_x, length_y)
        
        # 편의점 까지 가기
        while length_x > 0:
            beer -= 1
            length_x -= 50
            start[0] += 50
            #print(beer, length_x, start)
        while length_y > 0:
            beer -= 1
            length_y -= 50
            start[1] += 50
        
        # 맥주가 다 떨어지면 종료
        if beer < 0:
            print("sad")
            exit()
        
        # 편의점에 도착했으면 맥주 채우기
        if start[0] >= conv[i][0] and start[1] >= conv[i][1]:
            beer = 20
            continue
    
    # 목적지까지 가기
    length_x = end[0] - start[0]
    length_y = end[1] - start[1]
    
    while length_x > 0:
        beer -= 1
        length_x -= 50
        start[0] += 50
        #print(beer, length_x, start)
    while length_y > 0:
        beer -= 1
        length_y -= 50
        start[1] += 50
    
    if start[0] >= end[0] and start[1] >= end[1] and beer >= 0:
        print("happy")
    else:
        print("sad")
"""

from collections import deque

def bfs(start, visited):
    q = deque()
    q.append(start)
    
    while q:
        x, y = q.popleft()
        # 목적지 도달이 가능한 경우
        if abs(end[0]-x) + abs(end[1]-y) <= 1000:
            print("happy")
            return
        # 목적지 도달이 불가할 경우, 방문 가능한 편의점노드 추가하기
        for i in range(n):
            if abs(conv[i][0]-x) + abs(conv[i][1]-y) <= 1000 and not visited[i]:
                q.append([conv[i][0], conv[i][1]])
                visited[i] = 1
    print("sad")
    return

t = int(input())
for _ in range(t):
    n = int(input())
    start = list(map(int, input().split()))
    conv = []
    for _ in range(n):
        conv.append(list(map(int, input().split())))
    end = list(map(int, input().split()))

    visited = [0]*n
    bfs(start, visited)