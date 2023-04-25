"""
n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)

total = 0
while nums:
    if len(nums) > 1 and nums[0] > 1 and nums[1] > 1:
        total += nums[0]*nums[1]
        del nums[0]
        del nums[0]
    elif nums[0] == 1:
        total += 1
        del nums[0]
    elif nums[0] == 0 and len(nums) > 1 and len(nums)%2 == 0:
        del nums[0]
        del nums[1]
    else:
        total += nums[0]
        del nums[0]
print(total)
"""
# 그리디 - 1시간

n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)
plus = []
zero = 0
one = []
minus = []

# 음수, 0, 1, 양수 나누기
total = 0
for num in nums:
    if num > 1:
        plus.append(num)
    elif num == 1:
        one.append(num)
    elif num == 0:
        zero = 1
    elif num < 0:
        minus.append(num)

# 양수 값 처리
if len(plus)%2 == 0:
    for i in range(0, len(plus), 2):
        total += (plus[i]*plus[i+1])
else:
    total += plus[-1]
    del plus[-1]
    for i in range(0, len(plus), 2):
        total += (plus[i]*plus[i+1])

# 1 처리
if one:
    total += len(one)

# 음수 값 처리
if len(minus)%2 == 0:
    for i in range(0, len(minus), 2):
        total += (minus[i]*minus[i+1])
else:
    # 음수가 홀수개일 때 0이 있으면 0과 음수 최소 값을 곱한다.
    if zero == 1:
        del minus[0]
        if len(minus) > 1:
            for i in range(0, len(minus), 2):
                total += (minus[i]*minus[i+1])
    else:
        total += minus[0]
        del minus[0]
        if len(minus) > 1:
            for i in range(0, len(minus), 2):
                total += (minus[i]*minus[i+1])

print(total)