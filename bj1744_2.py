n = int(input())
nums = [int(input()) for _ in range(n)]
nums.sort(reverse=True)
plus = []
minus = []
one = 0
zero = 0
result = 0

for i in range(n):
    if nums[i] > 1:
        plus.append(nums[i])
    elif nums[i] == 1:
        one += 1
    elif nums[i] == 0:
        zero = 1
    elif nums[i] < 0:
        minus.append(nums[i])

if len(plus)%2 == 0:
    for i in range(0, len(plus), 2):
        result += (plus[i]*plus[i+1])
else:
    result += plus[-1]
    del plus[-1]
    for i in range(0, len(plus), 2):
        result += (plus[i]*plus[i+1])

result += one

if len(minus)%2 == 0:
    for i in range(0, len(minus), 2):
        result += (minus[i]*minus[i+1])
else:
    if zero:
        del minus[0]
        for i in range(0, len(minus), 2):
            result += (minus[i]*minus[i+1])
    else:
        result += minus[0]
        del minus[0]
        for i in range(0, len(minus), 2):
            result += (minus[i]*minus[i+1])
            
print(result)