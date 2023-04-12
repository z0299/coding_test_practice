n = int(input())

dp = [[1]*10 for _ in range(n+1)]
dp[0] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

if n >= 1:
    dp[1] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    for i in range(2, n+1):
        for j in range(10):
            count = 0
            for k in range(j+1):
                count += dp[i-1][k]
            dp[i][j] = count

print(dp[-1][-1]%10007)