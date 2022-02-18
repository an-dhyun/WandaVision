X = int(input())
line = 1
while True:
    if X-line <=0:
        num = line+1
        if line%2==0:
            print(str(X)+"/"+str(num-X))
        else:
            print(str(num-X)+"/"+str(X))
        break
    else: 
        X -= line
        line += 1