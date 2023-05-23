import heapq
from heapq import heapify
test = int(input())

while test != 0:
    test -= 1
    k = int(input())
    pages = list(map(int, input().split()))
    ans = 0
    
    heapify(pages)
    while len(pages) > 1:
        a = heapq.heappop(pages)
        b = heapq.heappop(pages)
        ans += (a + b)
        heapq.heappush(pages, a+b)
    print(ans)
        
    