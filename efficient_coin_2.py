n, m = map(int,input().split())
coin = [int(input()) for _ in range(n)]
dp = [10001]*(m+1)
dp[0] = 0

for c in coin:
    for i in range(c, m+1):
        dp[i] = min(dp[i], dp[i-c]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])