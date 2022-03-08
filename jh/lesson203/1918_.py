import sys
input = sys.stdin.readline

word = input().rstrip()
stack = []
string = ''

for i in word:
    if i.isalpha():
        string += i
    else:
        if i == '(':
            stack.append(i)
        elif i == '*' or '/': 
            # stack is not empty
            while stack and (stack[-1] == "*" or stack[-1] == '/'):
                string += stack.pop()
            stack.append(i)
        elif i == '+' or '-':
            # stack is not empty
            while stack and stack[-1] != '(':
                string += stack.pop()
            stack.append(i)
        elif i == ')':
            # stack is not empty, 
            while stack and stack[-1] != '(':
                string += stack.pop()
            stack.append(i)

while stack:
    string += stack.pop()

print(string)
