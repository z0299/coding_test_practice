n = int(input())
nums = list(map(int, input().split()))
nums2 = sorted(list(set(nums)))

idx = {nums2[i] : i for i in range(len(nums2))}
# print(idx)
for i in range(n):
    print(idx[nums[i]], end = ' ')