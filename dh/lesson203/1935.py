import sys
N = int(sys.stdin.readline())
sent = list(sys.stdin.readline().strip())
for i in range(65, 65+N):
    inp = int(sys.stdin.readline())
    for _ in range(sent.count(chr(i))):
        sent[sent.index(chr(i))] = inp

i = 0
while True:
    if len(sent)==1: break
    elif sent[i]=='*': 
        first = sent.pop(i-2)
        second = sent.pop(i-2)
        sent[i-2] = first*second
        i = i-2 + 1
    elif sent[i]=='+': 
        first = sent.pop(i-2)
        second = sent.pop(i-2)
        sent[i-2] = first+second
        i = i-2 + 1
    elif sent[i]=='-': 
        first = sent.pop(i-2)
        second = sent.pop(i-2)
        sent[i-2] = first-second
        i = i-2 + 1
    elif sent[i]=='/': 
        first = sent.pop(i-2)
        second = sent.pop(i-2)
        sent[i-2] = first/second
        i = i-2 + 1
    else: i += 1
print(format(sent[0],".2f"))