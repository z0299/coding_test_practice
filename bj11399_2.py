# greedy 알고리즘 공부 - 7분
import sys
input = sys.stdin.readline
n = int(input())
times = list(map(int, input().split()))
times.sort()
total_sum = 0
temp_sum = 0

for i in range(len(times)):
    temp_sum += times[i]
    total_sum += temp_sum
print(total_sum)