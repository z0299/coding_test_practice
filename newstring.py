# greedy 알고리즘 공부 - 30분 (테케에서 틀림) 다시보기
# 알파벳도 sort가 된다..! 그리고 isalpha함수를 활용해보자..

my_list = list(input())
sum_num = 0

for i in range(len(my_list)):
    if int(ord(my_list[i])) >= 65 and int(ord(my_list[i])) <= 90:
        my_list[i] = int(ord(my_list[i]))
    elif int(ord(my_list[i])) >= 49 and int(ord(my_list[i])) <= 57:
        my_list[i] = int(my_list[i])
        sum_num += my_list[i]
        
my_list.sort()
for i in my_list[:]:
    if i < 10:
        my_list.remove(i)

for i in range(len(my_list)):
    my_list[i] = chr(my_list[i])
my_list.append(str(sum_num))

print(''.join(my_list))

"""
data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.apend(x)
    else:
        value += int(x)
        
result.sort()

if value != 0:
    result.append(str(value))
    
print(''.join(result))
"""