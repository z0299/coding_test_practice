# 3:00~
"""
1. lost와 reserve에 같은 번호가 있으면, 여벌옷은 자기가 입어야 하므로 lost와 reserve에서 해당 학생 제외.
2. return = n-len(lost)
3. lost를 돌면서 lost-1이나 lost+1값이 reserve에 있으면, reserve에서 해당 번호를 제외.-> return += 1

틀린 이유: 내가 푼 방식대로 하려면, lost와 reserve가 sort되어있어야 한다! sort를 안해주면 greedy조건을 만족하지 못함.
"""
def solution(n, lost, reserve):
    # lost = reserve 제외
    for lost_stu in lost[:]:
        for reserve_stu in reserve[:]:
            if lost_stu == reserve_stu:
                lost.remove(lost_stu)
                reserve.remove(reserve_stu)

    answer = n - len(lost)
    lost.sort()
    reserve.sort()
    
    for lost_stu in lost:
        if lost_stu-1 in reserve:
            reserve.remove(lost_stu-1)
            answer += 1
            continue
        elif lost_stu+1 in reserve:
            reserve.remove(lost_stu+1)
            answer += 1
            continue
    
    return answer