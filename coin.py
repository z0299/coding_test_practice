def min_coin_count(value, coin_list):
    coin_count = 0
    
    coin_list.sort(reverse=True)    #sort정렬, 기본값은 오름차순 정렬, reverse=True옵션은 내림차순 정렬
    for coin in coin_list:
        coin_count += value // coin #나누기 연산 후 나머지 버림
        value = value % coin
    
    return coin_count
        
def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        details.append([coin, coin_num])
        value -= coin_num * coin
    return total_coin_count, details