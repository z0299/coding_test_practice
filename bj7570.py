"""
n = int(input())
nums = list(map(int, input().split()))
if n % 2 == 1:
    mid = n//2+1
else:
    mid = n//2
left = list(range(mid-1, 0, -1))
right = list(range(mid+1, n+1))
cnt = 0

for i in left:
    if nums[0:mid-1] == left:
        break
    else:
        cnt += 1
        idx = nums.index(i)
        nums.pop(idx)
        nums.insert(0, i)
    
for i in right:
    if nums[mid:n] == right:
        break
    else:
        cnt += 1
        idx = nums.index(i)
        nums.pop(idx)
        nums.append(i)
    
print(cnt-1)
"""

n = int(input())
nums = list(map(int, input().split()))
nums.insert(0, 0)
dp = [0]*(n+1)

for i in range(n):
    print(nums[i], nums[i+1])
    if nums[i]+1 == nums[i+1]:   
        dp[i] = dp[i-1]+1
    else:
        continue
print(dp)