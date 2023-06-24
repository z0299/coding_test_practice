def dfs(i, temp):
    temp.append(nums[i])
    if len(temp) == m:
        print(" ".join(map(str, temp)))
        return
    
    for j in range(i+1, n):
        dfs(j, temp)
        temp.pop()
        
n, m = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()

for i in range(n):
    temp = []
    dfs(i, temp)