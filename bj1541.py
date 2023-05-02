string = input()
result = 0

if '-' in string:
    string = list(string.split('-'))
    print(string)
    temp_list = []
    for i in range(len(string)):
        if '+' in string[i]:
            temp = list(map(int, string[i].split('+')))
            temp_list.append(sum(temp))
        else:
            temp_list.append(int(string[i]))
    for i in range(len(temp_list)):
        if i == 0:
            result = temp_list[i]
        else:
            result -= temp_list[i]
else:
    string = list(map(int, string.split('+')))
    result = sum(string)
print(result)