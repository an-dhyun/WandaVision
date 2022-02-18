N = int(input())
cnt = 0
for i in range(N):
    word = input()
    word = list(map(str, word))
    alps = []
    while True:
        here = word[0]
        alps.append(here)
        while True:
            print(word)
            if len(word)!=0 and word[0]==here: word.pop(0)
            else: break
        if len(word)==0: break
    before = len(alps)
    after = len(list(set(alps)))
    if before==after: cnt += 1
print(cnt)
    
    
    