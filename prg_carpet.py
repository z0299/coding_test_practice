def solution(brown, yellow):
    answer = []
    """
    nums = [(1, yellow)]
    for i in range(2, ((yellow)//2)+1):
    # for i in range(2, yellow):
        if yellow % i == 0:
            print(yellow//i, i)
            if i < yellow // i:
                nums.append((i, yellow // i))
    """
    nums = []
    for i in range(1, (yellow+1)):
        if yellow % i == 0:
            if i <= yellow // i:
                nums.append((i, yellow//i))
            else:
                break
    # print(nums)
    for x, y in nums:
        if (x+1)*2 + (y+1)*2 == brown and y >= x:
            answer = [y+2, x+2]

    return answer