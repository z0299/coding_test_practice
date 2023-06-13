# 11:40 ~
"""
def recursion(s, t):
    print(s, t)
    if s == t:
        print('1')
        exit()
    
    # 문자열을 뒤집고 뒤에 B 추가하기
    s_temp1 = s[::-1]+'B'
    if s_temp1 in t:
        recursion(s_temp1, t)
        
    # 문자열 뒤에 A 추가하기
    s_temp2 = s+'A'
    if s_temp2 in t:
        recursion(s_temp2, t)
        
    # 문자열에 A를 추가하고, 뒤집고 B 추가하기
    s_temp3 = s_temp2[::-1]+'B'
    if s_temp3 in t:
        recursion(s_temp3, t)

    print('return')
    return 0

s = input()
t = input()
answer = recursion(s, t)
print(answer)
"""

s = input()
t = input()

while len(t) >= len(s):
    if len(t) == len(s):
        if t == s:
            print(1)
        else:
            print(0)
    
    if t[-1] == 'A':
        t = t[:len(t)-1]
    elif t[-1] == 'B':
        t = t[:len(t)-1]
        t = t[::-1]
        