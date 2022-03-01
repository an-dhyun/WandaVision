n = int(input())

def hanoi(n, a, b, c): # a: from, c: to
    if n == 1:
        print(a, c)
    else:
        hanoi(n-1, a, c, b) # (n-1) blocks move to b(2), not destination
        print(a, c) # bottom block moves to c(3), destination
        hanoi(n-1, b, a, c) # (n-1) blocks move to c(3), destination
print(2**n - 1)
hanoi(n, 1, 2, 3)