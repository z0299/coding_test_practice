# 틀렸따!!!
"""
n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]
dp = [0]*(m+1)

for i in range(1, m+1):
    for j in money:
        if i % j == 0:
            if dp[i] == 0:
                dp[i] = i//j
            else:
                dp[i] = max(dp[i], i//j)
    if dp[i] == 0:
        dp[i] = -1
print(dp[m])
"""

n, m = map(int, input().split())
money = [int(input()) for _ in range(n)]
dp = [10001]*(m+1)
dp[0] = 0

for i in money:
    for j in range(i, m+1):
        if dp[j-i] != 10001:
            dp[j] = min(dp[j], dp[j-i]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])