import itertools

def solution(numbers):
    answer = 0
    
    nums = []
    nums_list = set()
    for n in numbers:
        nums.append(n)
        if n != 0:
            nums_list.add(int(n))
    
    for i in range(2, len(nums)+1):
        temp = list(map(list, itertools.permutations(nums, i)))
        for n in temp:
            if n[0] != 0:
                nums_list.add(int(''.join(n)))
                
    # print(nums_list)
    for n in nums_list:
        if n == 0 or n == 1:
            continue
        
        flag = 0
        for i in range(2, n):
            if n != i and n % i == 0:
                flag = 1
                break
        if flag == 0:
            # print(n)
            answer += 1
    
    return answer