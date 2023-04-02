# greedy 알고리즘 공부 - 32분

import sys
input = sys.stdin.readline

n = int(input())
m = list(map(int, input().split()))
count = 0

while len(m) > min(m):
    for i in range(min(m)):
        m.remove(next(i for i in m if i <= min(m)))
    count += 1
    
print(count)

"""이게 맞는 것 같다..
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것 부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가시키기
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(result) # 총 그룹의 수 출력
"""