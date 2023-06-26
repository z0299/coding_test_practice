import sys
n = int(sys.stdin.readline())
s = set()

for _ in range(n):
    temp = sys.stdin.readline().split()
    if len(temp) == 2:
        calc = temp[0]
        i = int(temp[1])
        
        if calc == 'add':
            s.add(i)
        
        if calc == 'remove':
            s.discard(i)
        
        if calc == 'check':
            if i in s:
                print('1')
            else:
                print('0')
        
        if calc == 'toggle':
            if i in s:
                s.remove(i)
            else:
                s.add(i)
                
    else:
        calc = temp[0]
        
        if calc == 'all':
            s = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        
        if calc == 'empty':
            s.clear()