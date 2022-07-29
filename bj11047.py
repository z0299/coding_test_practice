#greedy 알고리즘 공부 - #11047 동전 0

#문제 조건에서 금액 k의 최댓값이 1억이기 때문에, DP로는 만들기 힘들다.
#동전의 가치가 배수로 증가한다는 조건 때문에 그리디로 풀 수 있다. (배수가 아닌 경우엔 그리디 사용 불가)

def min_coin_count(value, coins):
    coin_count = 0
    
    coins.reverse() #리스트를 거꾸로 뒤집는다(sort는 하지 않고 그냥 뒤집음)
    for coin in coins:
        coin_count += value // coin
        value = value % coin
    return coin_count

n, k = input().split()  #n,k = map(int, input().split()) 으로도 가능하다
n = int(n)
k = int(k)
coins = list()

for i in range(n):
    coins.append(int(input()))
    
total_coin_count = min_coin_count(k, coins)
print(total_coin_count)