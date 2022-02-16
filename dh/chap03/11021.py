if __name__=="__main__":
    a = int(input())
    for i in range(a):
        x, y = map(int, input().split())
        print("Case #%s: %s"%(i+1, x+y))