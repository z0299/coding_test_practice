# 5:10 ~
s = list(input())
part_string = set()

for i in range(len(s)):
    part_string.add(s[i])
    temp_str = str(s[i])
    
    j = i + 1
    while j < len(s):
        temp_str += str(s[j])
        part_string.add(temp_str)
        j += 1

print(len(part_string))