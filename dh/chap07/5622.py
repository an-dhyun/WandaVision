S = input()
S = list(map(str, S))
for i in range(len(S)):
    here = S[i]
    if here in ['A', 'B', 'C']: S[i] = 2
    elif here in ['D', 'E', 'F']: S[i] = 3
    elif here in ['G', 'H', 'I']: S[i] = 4
    elif here in ['J', 'K', 'L']: S[i] = 5
    elif here in ['M', 'N', 'O']: S[i] = 6
    elif here in ['P', 'Q', 'R', 'S']: S[i] = 7
    elif here in ['T', 'U', 'V']: S[i] = 8
    elif here in ['W', 'X', 'Y', 'Z']: S[i] = 9
print(sum(S)+len(S))