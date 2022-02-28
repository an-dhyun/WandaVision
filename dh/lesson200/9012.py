import sys
T = int(sys.stdin.readline())
for i in range(T):
    sent = sys.stdin.readline()
    sent = sent.replace("\n", "")
    while True:
        if sent.find("()") != -1:
            sent = sent.replace("()", "")
        else: break
    if len(sent)==0: print("YES")
    else: print("NO")