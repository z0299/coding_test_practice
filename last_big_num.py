def solution(numbers):
    stack = []
    answer = [-1]*len(numbers)
    for i in range(len(numbers)):
        if not stack or numbers[i] <= stack[-1][1]:
            stack.append([i, numbers[i]])
        while stack and numbers[i] > stack[-1][1]:
            a, b = stack.pop()
            answer[a] = numbers[i]
        stack.append([i, numbers[i]])
        
    return answer