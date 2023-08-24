# 4:10 ~
def dfs(n):
    if len(temp) == 6:
        print(' '.join(map(str, temp)))
        return
    
    for i in range(n+1, k):
        visited[i] = 1
        temp.append(nums[i])
        dfs(i)
        visited[i] = 0
        del temp[-1]
        

while True:
    nums = list(map(int, input().split()))
    if nums[0] == 0:
        break
    k = nums[0]
    del nums[0]
    nums.sort()
    # print(nums)
    
    visited = [0]*k
    
    for i in range(k-6+1):
        visited[i] = 1
        temp = [nums[i]]
        dfs(i)
    print()
    