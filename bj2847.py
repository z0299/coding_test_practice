# 그리디 - 20분
n = int(input())
nums = []
for i in range(n):
    nums.append(int(input()))

cnt = 0
for i in range(n-1, 0, -1):
    while nums[i] <= nums[i-1]:
        cnt += 1
        nums[i-1] -= 1

print(cnt) 