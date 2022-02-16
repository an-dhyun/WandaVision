if __name__=="__main__":
    a = int(input())
    temp = a; time = 0
    while True:
        time += 1
        second = (a//10+a%10)%10
        first = a%10
        a = first*10 + second
        if a==temp: break
    print(time)

