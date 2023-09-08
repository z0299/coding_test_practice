# 10:40 ~ 10:44
def solution(citations):
    answer = -1
    citations.sort()
    # print(citations)
    for i in range(len(citations)):
        temp = min(citations[i], len(citations)-(i))
        # print(citations[i], len(citations)-(i))
        if answer < temp:
            answer = temp
    # print(answer)
    return answer