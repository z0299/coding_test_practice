def solution(sizes):
    answer = 0
    max1 = 0
    max2 = 0
    
    for i in range(len(sizes)):
        if sizes[i][0] >= sizes[i][1]:
            if max1 < sizes[i][0]: 
                max1 = sizes[i][0]
            if max2 < sizes[i][1]:
                max2 = sizes[i][1]
        else:
            if max1 < sizes[i][1]: 
                max1 = sizes[i][1]
            if max2 < sizes[i][0]:
                max2 = sizes[i][0]
    # print(max1, max2)
    answer = max1*max2
    
    return answer