if __name__=="__main__":
    N, X = map(int, input().split())
    input = input(); str = input.split()
    for i in range(N):
        if int(str[i])<X: 
            print(int(str[i]), end=' ')