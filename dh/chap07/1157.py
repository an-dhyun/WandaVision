word = input().upper()
word = list(map(str, word))
word_uni = list(set(word))
word_cnt = []
for i in word_uni:
    word_cnt.append(word.count(i))
word_mx = max(word_cnt)
if word_cnt.count(word_mx)==1:
    print(word_uni[word_cnt.index(word_mx)])
else: print("?")