import math

def checkif(a):
    check = 0
    while True:
        if a//(math.pow(10,check)) != 0: check += 1
        else: break

    if check == 1 or check == 2: return True # 한자리수/두자리수일 경우 무조거누한수임
    elif check == 0: return False
    else: # 세자리수 이상의 경우
        answer = True
        start = (a%100)//10 - a%10 # 10의자리수 - 1의자리수
        for i in range(1,check-1):
            first = a%math.pow(10,i+2)//math.pow(10,i+1)
            second = a%math.pow(10,i+1)//math.pow(10,i)
            if first-second != start: answer = False # 자릿수간 차가 start과 다르면 무조건 False
        return answer

if __name__=="__main__":
    a = int(input())
    list = [x for x in range(a+1)]
    answer = 0
    for i in list:
        if checkif(i)==True: answer += 1 # True인 것만 개수에 더함
    print(answer)
