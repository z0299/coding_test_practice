def solution(phone_book):
    answer = True
    """
    phone_book.sort(key=len)
    # print(phone_book)
    for i in range(len(phone_book)):
        for j in range(i+1, len(phone_book)):
            n = 0
            while n < len(phone_book[i]):
                # print(n)
                # print(phone_book[i][n], phone_book[j][n])
                if phone_book[i][n] != phone_book[j][n]:
                    break
                n += 1
            
            if n == len(phone_book[i]):
                return False
    """
    
    phone_book.sort()
    # print(phone_book)
    for i in range(len(phone_book)-1):
        if phone_book[i] < phone_book[i+1]:
            # if phone_book[i+1].startswith(phone_book[i]):
            if phone_book[i+1][:len(phone_book[i])] == phone_book[i]:
                return False
    
    return answer