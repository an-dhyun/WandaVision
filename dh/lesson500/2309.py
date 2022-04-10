import sys
heights = [int(sys.stdin.readline().strip()) for _ in range(9)]
h_sum = sum(heights)
h_len = len(heights)

for i in range(h_len-1):
    break_sign = 0
    for j in range(i+1, h_len):
        if h_sum - heights[i] - heights[j] == 100:
            heights.pop(i)
            heights.pop(j-1)
            break_sign = 1; break
    if break_sign: break

heights.sort()
print('\n'.join(list(map(str, heights))))
