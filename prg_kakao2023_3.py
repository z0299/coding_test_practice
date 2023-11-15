def solution(users, emoticons):
    answer = [0, 0]
    data = [10, 20, 30, 40]
    sale = []
    
    # dfs로 전체 할인율에 대한 배열 생성
    def dfs(tmp, d):
        if d == len(tmp):
            sale.append(tmp[:])
            return
        else:
            for i in data:
                tmp[d] = i
                dfs(tmp, d+1)
                
    dfs([0]*len(emoticons), 0)
    
    for i in range(len(sale)):
        people = 0
        money = 0
        temp = [0, 0]
        for p in range(len(users)):
            total = 0
            for j in range(len(emoticons)):
                if users[p][0] <= sale[i][j]:
                    total += int(emoticons[j]*((100-sale[i][j])*0.01))

            if total >= users[p][1]:
                temp[0] += 1
            else:
                temp[1] += total
        
        if temp > answer:
            answer = temp

    return answer