#greedy 알고리즘 공부 - #11000 강의실 배정
#priority queue 작동원리 익혔던 문제!!
import heapq    #priorityqueue 제공 (오름차순으로 힙 구성, 제거는 가장 작은 값부터 제거)
import sys      #python 사용하여 코테 시 입력값 빠르게 받기 위해 반드시 사용!

n = int(sys.stdin.readline())
class_list = list()
for i in range(n):
    class_list.append(list(map(int,sys.stdin.readline().split())))
class_list.sort()  #인덱스 0기준 오름차순 정렬, 같은 경우 인덱스 1기준 오름차순 정렬

class_queue = list()    #priority queue
heapq.heappush(class_queue, class_list[0][1])

for i in range(1, n):
    if class_list[i][0] < class_queue[0]:   #class_queue[0]은 항상 최소값을 가지고 있기 때문에 
            heapq.heappush(class_queue, class_list[i][1])
    else:
        heapq.heappop(class_queue)
        heapq.heappush(class_queue, class_list[i][1])

print(len(class_queue))
