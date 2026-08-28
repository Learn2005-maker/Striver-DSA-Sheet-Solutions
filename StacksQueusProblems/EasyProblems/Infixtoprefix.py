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
        if ch.isalnum():
            postfix += ch
        elif ch == '(':
            stack.append(ch)
        elif ch == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            if stack:
                stack.pop()  # remove '('
        else:
            # Pop higher or equal precedence operators
            while (stack and stack[-1] != '(' and 
                  (precedence(stack[-1]) > precedence(ch) or 
                  (precedence(stack[-1]) == precedence(ch) and ch == '^'))):
                      postfix += stack.pop()
            # Push the current operator onto the stack
            stack.append(ch)
            
    # This must be outside the for loop!
    while stack:
        postfix += stack.pop()
        
    return postfix


def infix_to_prefix(expression):
    # Step 1: Reverse the infix expression
    expression = expression[::-1]
    temp = ""
    
    # Step 2: Swap parenthesis
    for ch in expression:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
        else:
            temp += ch
            
    # Step 3: Get postfix of the modified expression
    postfix = infix_to_postfix(temp)   
    
    # Step 4: Reverse the postfix to get the prefix
    return postfix[::-1]
        

expression = "F+D-C*(B+A)"
print("Infix:", expression)
print("Prefix:", infix_to_prefix(expression))
