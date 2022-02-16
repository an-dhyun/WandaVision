import sys
if __name__=="__main__":
    a = int(sys.stdin.readline())
    for i in range(a):
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)