# 8:45 ~ 9:20
def to_str(lst):
    return str(lst[0])+str(lst[1])

num = list(input())
new_num = num
count = 0

while True:
    count += 1
    
    if len(new_num) < 2:
        new_num.append('0')
        temp = new_num[0]
        new_num[0] = '0'
        new_num[1] = temp

    sum_num = list(str(int(new_num[0]) + int(new_num[1])))
    new_num = list(new_num[1]+sum_num[-1])
    
    if to_str(num) == to_str(new_num):
        break
    
print(count)

