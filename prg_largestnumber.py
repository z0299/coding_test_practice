# from itertools import permutations
def solution(numbers):
    answer = ''
    numbers.sort(key = lambda x:str(x)*3, reverse = True)
    
    for i in numbers:
        answer += str(i)
    return str(int(answer))
    
    """
    p = list(permutations(numbers))
    answer = 0
    for perms in p:
        perms = list(map(str, perms))
        if int(''.join(perms)) > answer:
            answer = int(''.join(perms))
    
    return str(answer)
    """