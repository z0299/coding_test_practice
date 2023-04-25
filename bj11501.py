"""
test = int(input())
for _ in range(test):
    n = int(input())
    cost = list(map(int, input().split()))
    
    result = 0
    for i in range(n):
        benefit = 0
        for j in range(i+1, n):
            if cost[j] > cost[i] and cost[j]-cost[i] > benefit:
                benefit = cost[j]-cost[i]
        result += benefit
    
    print(result)
"""
"""
from collections import deque

test = int(input())
for _ in range(test):
    n = int(input())
    cost = deque(list(map(int, input().split())))
    
    result = 0
    while cost:
        max_num = max(cost)
        index = cost.index(max_num)
        if index == 0:
            cost.popleft()
        for i in range(index):
            result += (max_num-cost[0])
            cost.popleft()
    print(result)
"""
test = int(input())
for _ in range(test):
    n = int(input())
    cost = list(map(int, input().split()))
    
    result = 0
    max = 0
    for i in range(n-1, -1, -1):
        if max < cost[i]:
            max = cost[i]
        elif max > cost[i]:
            result += (max - cost[i])
    print(result)