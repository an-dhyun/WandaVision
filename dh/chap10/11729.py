N = int(input())
def move(N, A, B, C):
    if N == 1:
        print(A, C)
    else:
        move(N - 1, A, C, B)
        print(A, C)
        move(N - 1, B, A, C)
print(2**N -1)
move(N, 1, 2, 3)