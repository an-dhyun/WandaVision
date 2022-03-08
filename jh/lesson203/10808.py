import sys
input = sys.stdin.readline

s = input().rstrip()
numbers = [0] * 26

for i in s:
    numbers[ord(i) - 97] = s.count(i)

print(*numbers)