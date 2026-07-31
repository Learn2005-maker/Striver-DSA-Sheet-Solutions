def postfix_to_infix(exp):
    stack=[]
    for ch in exp[::-1]:
        # If the character is an operand, push it to the stack
        if ch.isalnum():
            stack.append(ch)
        else:
            t1=stack.pop()
            t2=stack.pop()
            # Note the order: t1 comes before t2
            convertedstr='('+t1+ch+t2+')'
            stack.append(convertedstr)
    return stack[-1]        
    
expression = "*+ABC"
print(postfix_to_infix(expression))            