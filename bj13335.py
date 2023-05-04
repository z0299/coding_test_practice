from collections import deque
# n: 트럭 수, w: 다리 길이, l: 다리 최대 하중
n, w, l = map(int, input().split())
truck = deque(list(map(int, input().split())))
bridge = deque()
done = []
time = 0
weight = 0

while truck or bridge:
    time += 1
    
    # 다리위의 트럭 한칸씩 옮기기
    for i in range(len(bridge)):
        bridge[i][1] += 1
        
    # 다 건넌 트럭 done으로 옮기기
    if bridge and bridge[0][1] > w:
        weight -= bridge[0][0]
        done.append(bridge.popleft())

    # 트럭 다리위에 올리기
    if truck and weight + truck[0] <= l:
        weight += truck[0]
        bridge.append([truck.popleft(), 1])
    
print(time)
        