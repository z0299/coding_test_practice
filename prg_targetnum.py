def solution(numbers, target):
    answer = 0
    
    def dfs(index, total):
        if index == len(numbers):
            if total == target:
                nonlocal answer
                answer += 1
                return
        else:
            dfs(index+1, total+numbers[index])
            dfs(index+1, total-numbers[index])
    
    dfs(0, 0)
    return answer