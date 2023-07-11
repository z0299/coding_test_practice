n = int(input())
nums = list(map(int, input().split()))
nums2 = sorted(list(set(nums)))

dict = {}
for i in range(len(nums2)):
    dict.update({nums2[i] : i})

for i in range(n):
    print(dict[nums[i]], end=' ')