def prefix_to_postfix(exp):
    stack=[]
    for ch in exp[::-1]:
        if ch.isalnum():
            stack.append(ch)
        else:
            t1=stack.pop()
            t2=stack.pop()
            convertedstr=t1+t2+ch
            stack.append(convertedstr)
    return stack[-1]
    
exp = "*+AB-CD"
print(f"Prefix: {exp}")
print(f"Postfix:  {prefix_to_postfix(exp)}")
    
    