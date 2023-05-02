"""
def solution(targets):
    targets.sort()
    answer = 0
    print(targets)
    now = [-1, -1]
    for i in range(len(targets)):
        print(now)
        if targets[i][0] >= now[1]:
            answer += 1
            now = targets[i]
        else:
            if now[1]-now[0] > targets[i][1]-targets[i][0]:
                now = targets[i]
            continue
    return answer
"""
def solution(targets):
    targets.sort(key = lambda x: [x[1], x[0]])
    answer = 0
    end = -1
    
    for i in range(len(targets)):
        if end <= targets[i][0]:
            answer += 1
            end = targets[i][1]
    
    return answer