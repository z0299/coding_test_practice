# 아 이거 너무 어려웠다..
test_num = int(input())
result_list = []

for _ in range(test_num):
    result = []
    n = int(input())
    
    # min_num
    dp_min = [0]*101
    dp_min[2] = '1'
    dp_min[3] = '7'
    dp_min[4] = '4'
    dp_min[5] = '2'
    dp_min[6] = '6'
    dp_min[7] = '8'
    
    dp_min[8] = '10'
    dp_min[9] = '18'
    dp_min[10] = '22'
    dp_min[11] = '20'
    dp_min[12] = '28'
    dp_min[13] = '68'
    
    dp_min[17] = '200'
    
    if n > 13:
        if n % 7 == 0:
            dp_min[n] = dp_min[7] + ('8'*(n//7-1))
        if n % 7 == 1:
            dp_min[n] = dp_min[8] + ('8'*(n//7-1))
        if n % 7 == 2:
            dp_min[n] = dp_min[9] + ('8'*(n//7-1))
        if n % 7 == 3:
            if n > 17:
                dp_min[n] = dp_min[17] + ('8'*(n//7-2))
        if n % 7 == 4:
            dp_min[n] = dp_min[11] + ('8'*(n//7-1))
        if n % 7 == 5:
            dp_min[n] = dp_min[12] + ('8'*(n//7-1))
        if n % 7 == 6:
            dp_min[n] = dp_min[13] + ('8'*(n//7-1))
    
    result.append(dp_min[n])
    
    # max_num
    digit = n // 2
    left = n % 2
    result_max = ''
    
    if left == 1:
        result_max = '7'
    elif left == 0:
        result_max = '1'
    
    while digit > 1 :
        result_max += '1'
        digit -= 1
    
    result.append(result_max)
    result_list.append(result)
    
for i in range(len(result_list)):
    print(' '.join(result_list[i]))