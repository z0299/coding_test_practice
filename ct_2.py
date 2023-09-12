def solution(n, m, send, errorlog):
    answer = [0]*len(send)
    fail = []
    late = []
    for i in range(len(errorlog)):
        if errorlog[i][0] == 1:
            fail.append(errorlog[i][1])
        elif errorlog[i][0] == 2:
            late.append(errorlog[i][1])
    
    for i in range(len(send)):
        mail = send[i]
        
        # 전송 1
        mail += n
        
        # 작업
        left_time = m
        while left_time > 0:
            if mail in fail:
                answer[i] = -1
                break
            if mail in late:
                left_time *= 2
            
            mail += 1
            left_time -= 1
            
        # 전송 2
        mail += n
        
        if answer[i] == 0:
            answer[i] = mail
            
    return answer