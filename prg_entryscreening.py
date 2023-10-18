# 8:00~
def solution(n, times):
    min_val = 1
    max_val = max(times)*n
    answer = 0
    
    while min_val <= max_val:
        mid_val = (min_val+max_val)//2
        ans = 0
        for time in times:
            ans += mid_val//time
        if ans >= n:
            answer = mid_val
            max_val = mid_val-1
        elif ans < n:
            min_val = mid_val+1
            
    return answer