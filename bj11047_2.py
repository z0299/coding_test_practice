# greedy 알고리즘 공부 - 15분 - 동전 0 - 다시 풀어보기..

import sys
input = sys.stdin.readline
coin = []
count = 0
n, k = map(int, input().split())

for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)

for i in range(n):
    count += k // coin[i]
    k = k % coin[i]
    # if k >= coin[i]:
    #     count += (k //)
    #     while k >= coin[i]:
    #         count += 1
    #         k -= coin[i]
    # else:
    #     continue
print(count)