import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        mix = heapq.heappop(scoville) + (heapq.heappop(scoville)*2)
        heapq.heappush(scoville, mix)
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < K:  # 음식이 1개 남을 때까지 합쳤는데, 최소가 K보다 작은 경우
            return -1
    
    return answer 