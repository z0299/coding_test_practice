# 2:25~
from collections import deque

n = int(input())
k = int(input())
sensor = list(map(int, input().split()))
sensor.sort()
dist = []

for i in range(n-1):
    dist.append(sensor[i+1]-sensor[i])
dist.sort(reverse=True)
dist = deque(dist)

if n > k:
    for _ in range(k-1):
        dist.popleft()
    print(sum(dist))
else:
    print(0)
