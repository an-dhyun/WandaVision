if __name__=="__main__":
    try:
        while True:
            a, b = map(int, input().split())
            print(a+b)
            continue
    except:
        exit() # EOF: end of file으로, 입력이 없으면 끝내는 처리