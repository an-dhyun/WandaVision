import sys
input = sys.stdin.readline

n = int(input())
word = input().rstrip()
numbers = [0]*n

for i in range(n):
    numbers[i] = int(input())

stack = []

for i in word:
    if 'A' <= i <= 'Z':
        stack.append(numbers[ord(i)-ord('A')])
    else:
        str2 = stack.pop()
        str1 = stack.pop()

        if i == '+':
            stack.append(str1+str2)
        elif i == '-':
            stack.append(str1-str2)
        elif i == '*':
            stack.append(str1*str2)
        elif i == '/':
            stack.append(str1/str2)

print('%.2f' %stack[0])