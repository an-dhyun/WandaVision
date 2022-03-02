x, y, w, h = map(int, input().split())
list = [x, y, abs(x-w), abs(y-h)]
print(min(list))