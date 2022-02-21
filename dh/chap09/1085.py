x, y, w, h = map(int, input().split())
nums = [x, y, abs(w-x), abs(h-y)]
print(min(nums))