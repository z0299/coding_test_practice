s = input()

result = 0
if '-' in s:
    nums = s.split('-')
    temp = []
    for i in range(len(nums)):
        if '+' in nums[i]:
            temp_2 = nums[i].split('+')
            temp_sum = 0
            for j in range(len(temp_2)):
                temp_sum += int(temp_2[j])
            temp.append(temp_sum)
        else:
            temp.append(int(nums[i]))
    for i in range(len(temp)):
        if i == 0:
            result = temp[i]
        else:
            result -= temp[i]
else:
    nums = list(map(int, s.split('+')))
    for i in range(len(nums)):
        result += nums[i]
print(result)