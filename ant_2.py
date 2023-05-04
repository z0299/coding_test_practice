"""
n = int(input())
foods = list(map(int, input().split()))
dp = [0]*(n+1)
dp[1] = foods[0]
dp[2] = max(foods[0], foods[1])

for i in range(1, n+1):
    for j in range(1, i-1):
        tul = foods[i-1] + dp[j]
        max_num = max(tul, dp[i-1])
        dp[i] = max_num
        # 틀린풀이다. 왜냐하면 DP테이블의 성질을 제대로 활용하지 못했다.
        # 최대 2개만 터는 코드를 짜버렸다. (슬라이딩 윈도우 처럼)
        # if dp[i] < dp[j] + foods[i-1]:
        #     dp[i] = dp[j] + foods[i-1]

print(dp[n])
"""
n = int(input())
array = list(map(int, input().split()))

dp = [0]*100
dp[0] = array[0]
dp[1] = max(array[0], array[1])

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-2]+array[i])

print(dp[n-1])