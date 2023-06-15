# 11:20 ~
l, c = map(int, input().split())
words = list(input().split())
words.sort()
answer = []

def back_tracking(idx):
    if len(answer) == l:
        vowel = 0
        const = 0
        
        for i in range(l):
            if answer[i] in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
            else:
                const += 1
        
        if vowel >= 1 and const >= 2:
            print("".join(answer))
            
        return
    
    for i in range(idx, c):
        answer.append(words[i])
        back_tracking(i+1)
        answer.pop()
 
back_tracking(0)
