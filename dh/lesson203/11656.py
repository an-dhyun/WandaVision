import sys
S = list(sys.stdin.readline().strip())
words = []
for i in range(len(S)):
    words.append(''.join(S[i:]))
words.sort()
print('\n'.join(words))