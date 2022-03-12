n, m = map(int, input().split())

# combination = n! / m!(n-m)!
# 10 = 2 * 5

def cnt_num(n, k):
    cnt = 0
    while n: # repeat n times
        n //= k
        cnt += n
    return cnt

two = cnt_num(n, 2) - cnt_num(m, 2) - cnt_num(n-m, 2)
five = cnt_num(n, 5) - cnt_num(m, 5) - cnt_num(n-m, 5)

print(min(two, five))