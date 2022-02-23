import sys
N = int(sys.stdin.readline())
words = []
for i in range(N):
    word = sys.stdin.readline()
    words.append(word)
words = list(set(words))
words.sort(key = lambda x : (len(x), x))

for i in words:
    print(i, end='')