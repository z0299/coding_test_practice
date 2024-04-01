import sys
n = int(sys.stdin.readline())
ans = []

for _ in range(n):
    s1, s2 = map(str, input().split())
    # s1, s2 = input().split()
    
    for idx, s in enumerate(s1):
        if s == 'x' or s == 'X':
            ans.append(s2[idx].upper())
            break
    """ string이랑 list를 사용하는 것 사이에 속도차이가 왜 이렇게 심하게 나냐..?
    for idx, s in enumerate(s1):
        if s == 'x' or s == 'X':
            ans += s2[idx].upper()
            break
    """

print(''.join(ans))

"""
for i in range(n):
    s1, s2 = input().split()
    s1 = list(s1.lower())
    s2 = list(s2.lower())

    idx = s1.index('x')
        
    ans +=  s2[idx].upper()
print(ans)
"""

import sys
n = int(sys.stdin.readline())
ans = ''

for i in range(n):
    s1, s2 = input().split()
    s1 = list(s1.lower())
    s2 = list(s2.lower())

    idx = s1.index('x')
        
    ans +=  s2[idx].upper()
    """
    for j in range(len(s1)):
        if s1[j] == 'x' or s1[j] == 'X':
            ans += s2[j].upper()
    """
print(ans)