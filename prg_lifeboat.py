def solution(people, limit):
    answer = 0
    people.sort(reverse = True)
    # print(people, limit)
    for p in people:
        answer += 1
        if p + people[-1] <= limit:
            del people[-1]
        # print(people)
    return answer