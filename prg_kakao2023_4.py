# 풀이 보고 풀었는데 잘 모르겠다.. (포화이진트리 만드는 부분)
def solution(numbers):
    answer = []
    def isvalid(x):
        if len(x) == 1:
            return True
        
        if x[len(x)//2] == '0':
            return x.count('0') == len(x)
        else:
            return isvalid(x[:len(x)//2]) and isvalid(x[len(x)//2+1:])
    
    for num in numbers:
        flag = 0
        
        for n in range(1, 7):
            rep = bin(num)[2:]
            if len(rep) > 2**n-1:
                continue
            
            rep = rep.rjust(2**n-1, '0')
            if isvalid(rep):
                flag = 1
    
        answer.append(flag)

    return answer