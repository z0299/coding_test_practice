n = int(input())
food_list = list(map(int, input().split()))

dp = [0]*n

dp[0] = food_list[0]
dp[1] = max(food_list[0], food_list[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+food_list[i])
    
print(dp[n-1])