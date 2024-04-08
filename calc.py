from stack import *
import re


number = r"(\d+)|-(\d+)"
operator = r"((\+)|(\-)|(\*))"
opdict = {"+": lambda a, b: a + b, "-": lambda a, b: a - b, "*": lambda a, b: a * b}
stack = Stack()

while True:
    str = input("Enter a postfix expression: ")

    tokens = re.split(r"\s+", str)

    for token in tokens:
        if re.match(number, token):
            stack.push(int(token))
            continue

        if re.match(operator, token):
            b = stack.pop()
            a = stack.pop()
            stack.push(opdict[token](a, b))
            continue

    if len(stack) > 1:
        print("Incomplete postfix expression")
        stack.reset()
        continue

    print(stack.pop())
