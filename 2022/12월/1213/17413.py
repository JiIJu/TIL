# 17413 단어뒤집기2

S = list(input())

ans = []
i = 0
start = 0
while i<len(S):
    if S[i]=='<':
        while S[i]!='>':
            i+=1
        i+=1
    elif S[i]== ' ':
        i+=1
    else:
        start= i
        while i<len(S) and S[i]!=' ' and S[i] != '<' and S[i] != '>':
            i+=1
        tmp = S[start:i]
        S[start:i] = tmp[::-1]
print(''.join(S))