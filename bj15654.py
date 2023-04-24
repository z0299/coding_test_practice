n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
visited = [0]*n

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, result)))

    for i in range(n):
        if not visited[i]:
            result.append(nums[i])
            visited[i] = 1
            dfs(depth+1)
            result.pop()
            visited[i] = 0

dfs(0)