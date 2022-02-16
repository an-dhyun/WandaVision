if __name__=="__main__":
    a, b = map(int, input().split())
    if b>=45: print("%s %s"%(a, b-45))
    elif b<45: 
        if a>0: print("%s %s"%(a-1, 60-(45-b)))
        elif a==0: print("%s %s"%(23, 60-(45-b)))