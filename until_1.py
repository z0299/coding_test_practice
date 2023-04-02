# greedy 알고리즘 공부 - 6분

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count = 0
while n != 1:
    if n % k == 0:
        n = n/k
        count += 1
    else:
        n = n - 1
        count += 1
print(count)

"""
만약 10억이 넘어가는 수라면, 아래와 같이 테크닉을 써야한다.
시간을 log까지 줄여준다.
while True:
    target = (n//k)*k
    result += (n-target)
    n = target
    
    if n < k:
        break
        
    result += 1
    n //=k
    
result += (n-1)
print(result)
"""