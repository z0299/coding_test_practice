#greedy 알고리즘 공부 - #2217 로프

import sys
input = sys.stdin.readline

n = int(input())
weight_list = []
for i in range(n):
    weight_list.append(int(input()))
weight_list.sort(reverse=True)
max_weight_array = []

for i in range(len(weight_list)):
    if i < len(weight_list)-1 and weight_list[i] == weight_list[i+1]:
        continue
    max_weight_array.append(weight_list[i]*(i+1))
print(max(max_weight_array))