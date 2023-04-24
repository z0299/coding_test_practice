""" 시간초과
get_string = input()
bomb_str = input()

while True:
    if not get_string:
        print("FRULA")
        break
    if bomb_str not in get_string:
        print(get_string)
        break
    
    string_list = get_string.split(bomb_str)
    get_string = ''
    for i in range(len(string_list)):
        get_string += string_list[i]
"""

string = input()
bomb = input()

stack = []

for char in string:
    stack.append(char)
    if char == bomb[-1] and ''.join(stack[-(len(bomb)):]) == bomb:
        del stack[-(len(bomb)):]

answer = ''.join(stack)

if not answer:
    print("FRULA")
else:
    print(answer)