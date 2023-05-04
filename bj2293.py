n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)]
dp = [0]*(k+1)
dp[0] = 1 #동전이 1개 쓰이는 경우

for c in coin:
    for i in range(c, k+1):
        if i - c >= 0:
            dp[i] = dp[i] + dp[i-c]

print(dp[k])