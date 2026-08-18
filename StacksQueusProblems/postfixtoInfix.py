def postfix_to_infix(exp):
    stack=[]
    for ch in exp:
        # If the character is an operand, push it to the stack
        if ch.isalnum():
            stack.append(ch)
        else:
            t1=stack.pop()
            t2=stack.pop()
            convertedstr='('+t2+ch+t1+')'
            stack.append(convertedstr)
    return stack[-1]        
    
            
expression = "AB+C*"
print(postfix_to_infix(expression))            