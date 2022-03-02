import sys
input = sys.stdin.readline

S = list(input().rstrip())

i = 0
j = 0

while i < len(S):
    # find bar
    if S[i] == "(":
        i += 1
        while S[i] != ")":
            i += 1
        i += 1
    
    # find numbers or alphabet
    elif S[i].isalnum():
        j = i
        while i < len(S) and S[i].isalnum(): # not space and <>
            i += 1
        tmp = S[j:i]
        tmp.reverse()
        S[j:i] = tmp
    
    # find space
    else:
        i += 1
