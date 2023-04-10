# 우선순위 큐 -> Heap으로 구현
# heap의 heap[0](최상단)은 항상 최소값이다!
import sys
from heapq import heappush
from heapq import heappop

input = sys.stdin.readline
n = int(input())
class_list = []
for i in range(n):
    class_list.append(list(map(int, input().split())))
class_list.sort()  
classroom = 1
heap = []

heappush(heap, class_list[0][1])

for i in range(1, n):
    if class_list[i][0] >= heap[0]:
        heappop(heap)
        heappush(heap, class_list[i][1])
    else:
        classroom += 1
        heappush(heap, class_list[i][1])
print(classroom)
