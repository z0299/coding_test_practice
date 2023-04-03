#greedy 알고리즘 공부 - #2785 대회 or 인턴 - 11분

import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
total = n+m
count = n // 2
if m < count:
    count = m

while total-(count*3) < k:
    count -= 1
    
print(count)