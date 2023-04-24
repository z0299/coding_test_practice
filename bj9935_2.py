string = list(input())
bomb = list(input())
stack = []

for i in range(len(string)):
    stack.append(string[i])
    if stack[-len(bomb)::] == bomb:
        del stack[-len(bomb)::]

if stack:
    print(''.join(map(str, stack)))
else:
    print("FRULA")