#greedy 알고리즘 공부 - 책예제 = 1이 될 때까지

import sys
input = sys.stdin.readline

n, k = map(int, input().split())

count = 0
while n != 1:
    if n % k == 0:
        count += 1
        n /= k
    else:
        count += 1
        n -= 1
        
print(count)