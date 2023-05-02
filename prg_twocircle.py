def solution(r1, r2):
    answer = 0
    
    min_y, max_y = r1, r2
    
    for x in range(r2):
        while x**2 + max_y**2 > r2**2:
            max_y -= 1
        while min_y-1 and x**2 + (min_y-1)**2 >= r1**2:
            min_y -= 1
        answer += (max_y-min_y)+1
    
    """
    # 경계의 점
    line = (r2 - r1) + 1
    answer += line * 4
    
    # x=y
    xy = 0
    for i in range(r1, r2):
        xy += 1
    answer += xy * 4
    
    # 선과 xy 사이
    between = 0
    for i in range(r1, r2):
        for j in range(1, i):
            between += 1
    answer += between * 8
    """
    
    return answer*4