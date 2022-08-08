#greedy 알고리즘 공부 - #11399 ATM

import sys
input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
sum = 0

times.sort()
for i in range(n+1):
    for j in range(i):
        sum += times[j]
print(sum)