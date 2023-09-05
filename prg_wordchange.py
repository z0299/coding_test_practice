# 8:20 ~ 9:00
def dfs(cnt, words, begin, target, visited):
    global answer
    if begin == target:
        answer = min(answer, cnt)
        return cnt
    
    for word in words:
        count = [0, 0]
        if not visited[words.index(word)]:
            for i in range(len(begin)):
                if begin[i] != word[i]:
                    count[0] += 1
                    count[1] = i
            if count[0] == 1:
                visited[words.index(word)] = 1
                dfs(cnt+1, words, word, target, visited)
                visited[words.index(word)] = 0
            else:
                continue
    
answer = 1e9
def solution(begin, target, words):
    if target not in words:
        return 0
    
    visited = [0]*len(words)
    dfs(0, words, begin, target, visited)
    return answer