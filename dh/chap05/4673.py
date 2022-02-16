import math

def tens(a):
    check = 0
    while True:
        if a//(math.pow(10,check))!=0: check += 1
        else: break
    return check

def selfnum(a, check):
    answer = a
    for i in range(check):
        answer += int((a%math.pow(10,i+1))//math.pow(10,i))
    return answer

if __name__=="__main__":
    list = [x for x in range(1,10001)]
    num = 1
    while True:
        answer = selfnum(num, tens(num))
        if num<=10000: 
            try: list.remove(answer)
            except: pass
            num += 1
        else: break
    for i in list: print(i)
    
