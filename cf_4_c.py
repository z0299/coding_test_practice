# 해시 알고리즘 구현 (코드포스)
# 단점 - 테이블이 너무커서 디버깅이 어렵다..
HASH_SIZE = 1000
HASH_LEN = 400
HASH_VAL = 17   # key값이 겹치지 않게 하기 위해 주로 소수로 선언

index = [[0]*HASH_LEN for _ in range(HASH_SIZE)]    # 문자열이 저장된 개수를 저장
data = [[0]*HASH_LEN for _ in range(HASH_SIZE)]     # 문자열 저장
length = [0]*HASH_SIZE    # 문자열에 해당하는 Key 값이 들어온 개수를 저장

# key 값 얻기
def getHashKey(name):
    key = 0
    
    for c in name:
        key = (key*HASH_VAL) + ord(c) + HASH_VAL
        
    if key < 0:     # key가 음수이면 양수로 바꿔주기
        key = -key
        
    return key % HASH_SIZE

def checking(key, name):
    key_len = length[key]   # 문자열에 해당하는 Key 값이 들어온 개수
    
    if key_len != 0:    # key 값이 들어온적 있는 경우
        for i in range(key_len):    # 들어왔던 key 값 개수만큼 돌면서
            if name == data[key][i]:    # 일치하는 값이 있으면
                index[key][i] += 1
                return index[key][i]
    
    data[key][key_len] = name   
    length[key] += 1    # 해당 key 값에 들어온 개수 +1
    return -1

n = int(input())
for _ in range(n):
    name = input()
    key = getHashKey(name)
    cnt = checking(key, name)

    if cnt == -1:       # 해당 값이 저장된 적 없는 경우
        print("OK")
    else:               # 해당 값이 저장된 적 있는 경우
        print(f'{name}{str(cnt)}')