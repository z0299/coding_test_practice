from collections import deque

# test case개수와 결과 list 선언
test_num = int(input())
max_list = []

for _ in range(test_num):
    # 금광 지도 만들기
    n, m = map(int, input().split())
    temp_list = deque(list(map(int, input().split())))
    gold_map = [[] for _ in range(n)]
    for i in range(n):
        for _ in range(m):
            gold_map[i].append(temp_list.popleft())
    """
    slicing으로 금광지도 만드는 법
    index = 0
    for i in range(n):
        gold_map.append(temp_list[index:index+m])
        imdex += m
    """

    # DP 그래프 만들기
    dp = [[0]*m for _ in range(n)]
    for i in range(n):
        dp[i][0] = gold_map[i][0]
    
    # DP 실행 - 이전 열의 3가지 경우를 비교해 가장 큰 수와 현재 금 개수 더하기
    for y in range(1, m):
        for x in range(n):
            dp[x][y] = dp[x][y-1] + gold_map[x][y]
            if x-1 >= 0:
                dp[x][y] = max(dp[x][y], dp[x-1][y-1]+gold_map[x][y])
            if x+1 < n:
                dp[x][y] = max(dp[x][y], dp[x+1][y-1]+gold_map[x][y])
    
    # 최대 금 개수 찾기
    max_num = 0
    for i in range(n):
        for j in range(m):
            if max_num < dp[i][j]:
                max_num = dp[i][j]
    max_list.append(max_num)
    """
    max로 금 최대개수 찾기 - 마지막 열만 확인해주면 됐었다...!
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    """

for i in range(len(max_list)):
    print(max_list[i])