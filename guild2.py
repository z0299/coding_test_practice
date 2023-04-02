import sys
input = sys.stdin.readline

n = int(input())
my_list = list(map(int, input().split()))
my_list.sort()

group_count = 0
people_count = 0

for i in range(len(my_list)):
    people_count += 1
    if my_list[i] <= people_count:
        group_count += 1
        people_count = 0
print(group_count)