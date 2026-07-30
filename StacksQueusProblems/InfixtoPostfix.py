def precedence(op):
    if op == '^':
        return 3
    elif op == '*' or op == '/':
        return 2
    elif op == '+' or op == '-':
        return 1
    return 0


def infix_to_postfix(expression):
    stack = []
    postfix = ""

    for ch in expression:

        # Operand
        if ch.isalnum():
            postfix += ch

        # Left parenthesis
        elif ch == '(':
            stack.append(ch)

        # Right parenthesis
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Remove '('

        # Operator
        else:
            while (stack and stack[-1] != '(' and
                   precedence(stack[-1]) >= precedence(ch)):
                postfix += stack.pop()

            stack.append(ch)

    # Pop remaining operators
    while stack:
        postfix += stack.pop()

    return postfix


# Driver Code
exp = "A+B*(C-D)"
print("Infix :", exp)
print("Postfix :", infix_to_postfix(exp))


# This ensures expressions like A^B^C are converted correctly to:
# ABC^^

# while (stack and stack[-1] != '(' and
#        (precedence(stack[-1]) > precedence(ch) or
#         (precedence(stack[-1]) == precedence(ch) and ch != '^'))):
#     postfix += stack.pop()