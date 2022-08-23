#greedy 알고리즘 공부 - #1931 회의실 배정
#처음에 접근을 잘못했다. 회의 소요시간 기준 greedy가 아닌 종료시간 기준 greedy를 구현해야 했다.
#회의 소요시간 기준으로 풀이할 순 없을까...?
import sys

n = int(sys.stdin.readline())
class_list = list()
for i in range(n):
    class_list.append(list(map(int,sys.stdin.readline().split())))
    class_list[i].append(class_list[i][1]-class_list[i][0])
    
class_list.sort(key=lambda x:(x[1],x[0]))   #list의 [1]자리 기준 정렬, 이후 [0]자리 기준 정렬
using_list = list()
using_list.append(class_list[0][1])

for i in range(1,n):
    if class_list[i][0] >= using_list[0]:
        using_list.insert(0, class_list[i][1]) #insert(a,b): 리스트의 a자리에 b 요소 추가
    else:
        continue
print(len(using_list))